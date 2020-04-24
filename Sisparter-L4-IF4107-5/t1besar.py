# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()
# jika saya rank terbesar maka saya akan mengirimkan pesan ke proses yang mempunyai rank 0 s.d rank terbesar-1
if rank == 4:
    print("--- proses send oleh rank 4 ---")
    x = ("ini pesan dari rank 4","rank = ",rank,"size = ",size)
    print("send")
    comm.send(x, dest=0, tag=11)
    print("send")
    comm.send(x, dest=1, tag=11)
    print("send")
    comm.send(x, dest=2, tag=11)
    print("send")
    comm.send(x, dest=3, tag=11)
    print("--- proses send selesai ---")
# jika saya bukan rank terbesar maka saya akan menerima pesan yang berasal dari proses dengan rank terbesar
else:
    print("--- proses receive oleh rank ",rank,"---")
    x = comm.recv(source=4, tag=11)
    print("nilai x = ",x)
    print("pada rank = ",rank)
    print("total size = ",size)
    print("--- proses telah di terima oleh rank ",rank,"---")
