import requests
from bs4 import BeautifulSoup

CCFA = 1
CCFB = 0.5
CCFC = 0
COREASTAR = 2
COREA = 1
COREB = 0.5

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
def PPoPP():

    # ===================== PC =====================
    PCS = {}
    # https://ppopp19.sigplan.org/committee/PPoPP-2019-program-committee
    url_template = 'https://ppopp{}.sigplan.org/committee/PPoPP-{}-program-committee'
    for year in range(17,22):
        url = url_template.format(str(year),'20' + str(year))
        res = requests.get(url,headers).content
        soup = BeautifulSoup(res,"html.parser")
        for person in soup.find_all("h3",class_="media-heading"):
            PCS_name = 
            PCS.insert()
    
    url_2016 = 'https://ppopp16.sigplan.org/committee/ppopp-2016-papers-program-committee'
    



sysArch_CCF_A = {'PPoPP','FAST','DAC','HPCA','MICRO','SC','ASPLOS','ISCA','USENIX ATC'}
sysArch_CCF_B = {'SoCC','SPAA','PODC','FPGA','CGO','DATE','EuroSys','HOT CHIPS','CLUSTER','ICCD','ICCAD','ICDCS','CODES+ISSS','HiPEAC','SIGMETRICS','PACT','ICPP','ICS','VEE','IPDPS','Performance','HPDC','ITC','LISA','MSST','RTAS'}
sysArch_CCF_C = {'CF','SYSTOR','NOCS','ASAP','ASP-DAC','Euro-Par','ETS','FPL','FPL','GLSVLSI','ATS','HPCC','HiPC','MASCOTS','ISPA','CCGRID','NPC','ICA3PP','CASES','FPT','ICPADS','ISCAS','ISLPED','ISPD','HotI','VTS'}
Net_CCF_A = {'NSDI','INFOCOM'}
SE_CCF_A = {'SOSP','ICSE','OSDI'}

sys_CORE_ASTAR = {'ASPLOS','HPCA','INFOCOM','ICSA','OSDI','PODC','RTSS','SENSYS','SIGMETRICS','SOSP'}
sys_CORE_A = {'FAST','ATC','SPAA','PPoPP','CLUSTER','IPDPS','CCGRID','ICCAD','DSN','ICSA','ICDCS','ICPP','DISC','Eurosys','Middleware','SC','HPDC'}