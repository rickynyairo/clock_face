from multiprocessing import Process, Pipe

from flaskserver import run

parent_conn, child_conn = Pipe()
server_process = Process(target=run, args=(child_conn,))
server_process.start()
# convo = subprocess.run(flaskapp.run())
print(parent_conn.recv())

server_process.join()