import os
import pandas as pd

class MassiveProcessor:
    def __init__(self):
         # Set the path to the directory where the data files are located.
        self.directory_path = './1.1/data/'
         # List all files in the directory.
        self.files = [file for file in os.listdir(self.directory_path)]
         # Load the English dataset from 'en-US.jsonl' and filter out only the 'train' partition.
        # Also, set 'id' as the index and keep only the columns 'utt' and 'annot_utt'.
        self.en_df = pd.read_json(self.directory_path + 'en-US.jsonl', lines=True)
        self.en_df = self.en_df.loc[self.en_df['partition'] == 'train']
        self.en_df = self.en_df.set_index('id')
        self.en_df = self.en_df[['utt', 'annot_utt']]
        # Set the paths for output folders (Excel, JSONL, Pretty JSONL).
        self.folder_path_excel = './output/excel/'
        self.folder_path_jsonl = './output/jsonl/'
        self.folder_path_pretty = 'output/pretty/'

        # Check for output files. If they don't exist, create them.
        if not os.path.exists(self.folder_path_excel):
            os.makedirs(self.folder_path_excel)

        if not os.path.exists(self.folder_path_jsonl):
            os.makedirs(self.folder_path_jsonl)

        if not os.path.exists(self.folder_path_pretty):
            os.makedirs(self.folder_path_pretty)

    def process_excel_files(self):
        # Merge each file in the /data with the English dataframe 
        # Save the merged dataframe as an Excel file.
        for file in self.files:
            df = pd.read_json(self.directory_path + file, lines=True)
            df = df.set_index('id')
            df = df[['utt', 'annot_utt']]
            # Rename the columns to indicate the language.
            df = df.rename(columns={
                'utt': f'{file[:-9]}_utt',
                'annot_utt': f'{file[:-9]}_annot_utt'
            })
            #Merge English dataframe with the current dataframe
            merged_df = self.en_df.join(df)
            # Save to excel file
            file_name = f'{self.folder_path_excel}en-{file[:-9]}.xlsx'
            merged_df.to_excel(file_name)

    def process_jsonl_files(self):
        targets = ['en-US.jsonl', 'sw-KE.jsonl', 'de-DE.jsonl']
        categories = ['test', 'train', 'dev']

        for target in targets:
            path = self.directory_path + target
            df = pd.read_json(path, lines=True)
            for category in categories:
                filtered_df = df.loc[df['partition'] == category]
                destination = f'{self.folder_path_jsonl}{target[:-6]}-{category}.jsonl'
                filtered_df.to_json(destination, orient='records', indent=4, force_ascii=False)

    def process_pretty_jsonl(self):
        # Create JSONL file that shows translations 
        # from English to all other languages for the train partition.
        output_dict = {}
        # Drop the 'annot_utt' column from the English dataframe.
        self.en_df = self.en_df.drop(columns='annot_utt')
        

        for file in self.files:
            df = pd.read_json(self.directory_path + file, lines=True)
            df = df.loc[df['partition'] == 'train']
            df = df[['id', 'utt']]
            df = df.rename(columns={'utt': f'{file[:-9]}_utt'})

            merged_df = self.en_df.merge(df, on='id', how='outer')
            output_dict[file[:-9]] = merged_df.to_dict(orient='records')
        # Save the compiled translations to a JSONL file.
        destination = f'{self.folder_path_pretty}en_to_xx_train.jsonl'
        output_df = pd.DataFrame(output_dict)
        output_df.to_json(destination, orient='records', force_ascii=False, lines=True, indent=4)


