import os
import pandas as pd

class MassiveProcessor:
    def __init__(self):
        self.directory_path = './1.1/data/'
        self.en_df = pd.read_json(self.directory_path + 'en-US.jsonl', lines=True)
        self.en_df = self.en_df.loc[self.en_df['partition'] == 'train']
        self.en_df = self.en_df.set_index('id')
        self.en_df = self.en_df[['utt', 'annot_utt']]

        self.folder_path_excel = './output/excel/'
        self.folder_path_jsonl = './output/jsonl/'
        self.folder_path_pretty = 'output/pretty/'

        if not os.path.exists(self.folder_path_excel):
            os.makedirs(self.folder_path_excel)

        if not os.path.exists(self.folder_path_jsonl):
            os.makedirs(self.folder_path_jsonl)

        if not os.path.exists(self.folder_path_pretty):
            os.makedirs(self.folder_path_pretty)

    def process_excel_files(self):
        files = os.listdir(self.directory_path)
        files = [file for file in files]

        for file in files:
            df = pd.read_json(self.directory_path + file, lines=True)
            df = df.set_index('id')
            df = df[['utt', 'annot_utt']]
            df = df.rename(columns={
                'utt': f'{file[:-9]}_utt',
                'annot_utt': f'{file[:-9]}_annot_utt'
            })
            merged_df = self.en_df.join(df)

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
        files = os.listdir(self.directory_path)
        files = [file for file in files]

        output_dict = {}
        self.en_df = self.en_df.drop(columns='annot_utt')
        

        for file in files:
            df = pd.read_json(self.directory_path + file, lines=True)
            df = df.loc[df['partition'] == 'train']
            df = df[['id', 'utt']]
            df = df.rename(columns={'utt': f'{file[:-9]}_utt'})

            merged_df = self.en_df.merge(df, on='id', how='outer')
            output_dict[file[:-9]] = merged_df.to_dict(orient='records')

        destination = f'{self.folder_path_pretty}en_to_xx_train.jsonl'
        output_df = pd.DataFrame(output_dict)
        output_df.to_json(destination, orient='records', force_ascii=False, lines=True, indent=4)


