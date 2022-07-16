from plots import Data

class Constants:
    Vtho = 1.8383e+01;
    delta = 9.9000e-09;
    n = 5.5618e+01;
    l = 1.0250e+00;
    lam = 3.2560e+05;
    Vgcrit = 5.8974e+00;
    Jth = 1.0000e-02;
    Rso = 5.3378e+02;
    Vtun = 9.7119e-03;
    V0 = 9.8259e-03;
    Rmax = 2.1301e+04;
    Idleak=0.000000000774;
    W=0.1; #transistor width (cm)  
    typ=1; #type of transistor. nFET type=1; pFET type=-1
    kB=8.617e-5;        # Boltzmann constant [eV/K]
    Tjun=293;           #Junction temperature [K].
    phit = kB*Tjun; 
    shift=0 ;
    err = 1;
    i = 0;
    resnorm1min = 1;
    resnorm2min = 1;
    
constant=Constants()

class electricalcharcteristics:
    #transfer 1
    data=Data()
    file1 = data.data2Transfer3VF();
    Vds_1=3;
    Vds1 = abs(Vds_1);
    
    #transfer 2
    file2 = data.data2Transfer50VF();
    Vds_2=50;
    Vds2 = abs(Vds_2);
    
    #Output1
    file3 = data.data2output60v();
    Vgs_1=53.5-constant.shift;
    Vgs1 = abs(Vgs_1);
    
    #Output 2
    file4 = data.data2Output45V();
    Vgs_2=44.5-constant.shift;
    Vgs2 = abs(Vgs_2);
    
    #Output 3
    file5 = data.data2output30V();
    Vgs_3=31-constant.shift;
    Vgs3 = abs(Vgs_3);
    
EC=electricalcharcteristics()

    
coeff = [constant.Vtho, constant.delta, constant.n, constant.l, constant.lam, constant.Vgcrit, constant.Jth, constant.Rso, constant.Vtun, constant.V0, constant.Rmax]
gp = [constant.Idleak, constant.phit, constant.W, EC.Vds1, EC.Vds2, EC.Vgs1, EC.Vgs2, EC.Vgs3, constant.typ];

    

