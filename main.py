from classes.massiveProcessor import MassiveProcessor
from absl import app, flags
from multiprocessing import Process

FLAGS = flags.FLAGS
flags.DEFINE_boolean('background', False, 'Run in the background')

mp = MassiveProcessor()

def background_task():   
    mp.process_excel_files()
    pass


def main(argv):
    if FLAGS.background:
        background_process = Process(target=background_task)
        background_process.start()
    
        mp.process_jsonl_files()
        mp.process_pretty_jsonl()

if __name__ == '__main__':
    app.run(main)


