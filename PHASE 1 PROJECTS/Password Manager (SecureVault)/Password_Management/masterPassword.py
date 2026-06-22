import hashlib
import pwinput

M_A_S_T_E_RP_A_S_S_W_O_R_D = "79f06f8fde333461739f220090a23cb2a79f6d714bee100d0e4b4af249294619"

def authorize():
    while True:
        
        pwd = pwinput.pwinput(prompt="Password: ", mask="*")

        if hashlib.sha256(pwd.encode()).hexdigest() == M_A_S_T_E_RP_A_S_S_W_O_R_D:
            return True
        else:
            print("Incorrect Password.")