import configuration
import spin
import Projet_Code

'''Test for two and three spins'''
L=5
Beta=20
m=2
Jx=1
Jz=2
chess=Projet_Code.Chessboard(L, Beta, m, Jx, Jz)
conf=configuration.Configuration(chess)
print(conf.config)
chess._config_to_image()
#print(conf.get_energy(0))