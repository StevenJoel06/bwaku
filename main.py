from classes.massiveProcessor import MassiveProcessor
from absl import app, flags
from multiprocessing import Process

FLAGS = flags.FLAGS
# This flag determines if certain tasks should run in the background
flags.DEFINE_boolean('background', False, 'Run in the background')

mp = MassiveProcessor()

def background_task():  
    # Process Excel files using the MassiveProcessor instance 
    mp.process_excel_files()
    pass


def main(argv):
     # If the 'background' flag is set to True, start the background task
    if FLAGS.background:
        background_process = Process(target=background_task)
        background_process.start()
        # Regardless of the 'background' flag, process the JSONL files and pretty JSONL
        mp.process_jsonl_files()
        mp.process_pretty_jsonl()
#'main' function will run when the script is executed
if __name__ == '__main__':
    app.run(main)


