# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# jika saya rank ke 0 maka saya akan mengirimkan pesan ke proses yang mempunyai rank 1 s.d size
if rank == 0:
    print("--- proses send oleh rank 0 ---")
    x = ("ini pesan dari rank 4","rank = ",rank,"size = ",size)
    print("send ke 1")
    comm.send(x, dest=1,tag=11)
    print("send ke 2")
    comm.send(x, dest=2, tag=11)
    print("send ke 3")
    comm.send(x, dest=3, tag=11)
    
# jika saya bukan rank 0 maka saya menerima pesan yang berasal dari proses dengan rank 0
else:
    print("--- proses receive oleh rank ",rank,"---")
    y = comm.recv(source=0, tag=11)
    print("nilai x = ",y)
    print("pada rank = ",rank)
    print("total size = ",size)
    print("--- proses telah di terima oleh rank ",rank,"---")