import pyperclip, datetime

nonSponAccounts = '720101_zZz_720102_zZz_720103_zZz_720104_zZz_720105_zZz_720106_zZz_720107_zZz_720199_zZz_720203_zZz_720205_zZz_720206_zZz_720211_zZz_720212_zZz_720299_zZz_720303_zZz_720305_zZz_720306_zZz_720310_zZz_720311_zZz_720315_zZz_720318_zZz_720322_zZz_720399_zZz_720601_zZz_720602_zZz_720603_zZz_720604_zZz_720605_zZz_720606_zZz_720607_zZz_720608_zZz_720609_zZz_720610_zZz_720611_zZz_720702_zZz_720703_zZz_730106_zZz_730203_zZz_730207_zZz_730211_zZz_750101_zZz_750103_zZz_750105_zZz_750106_zZz_750199_zZz_770202_zZz_770251_zZz_770299_zZz_780199_zZz_781106_zZz_810101_zZz_810102_zZz_810201_zZz_810202_zZz_810203_zZz_810204_zZz_810205_zZz_850104'

addAnother = 'y'
today = datetime.datetime.today().strftime('%Y-%m-%d')

matterFileName = 'Matter-prod-A3F9-%s-0001.txt' % (today)
matterFilterFileName = 'MatterFilters-prod-A3F9-%s-0001.txt' % (today)
ackMatterFileName = 'Matter-prod-A3F9-%s-0001.ack' % (today)
ackFilterFileName = 'MatterFilters-prod-A3F9-%s-0001.txt' % (today)
matterFile = open(matterFileName, 'w')
matterFilterFile = open(matterFilterFileName, 'w')
ackMatterFile = open(ackMatterFileName, 'w')
ackFilterFile = open(ackFilterFileName, 'w')

def matterFilterFileCreate(f, d, p, c, fi):
   
    chartstring = '%s-%s-UMCIP-%s-1-%s_UMN01' %(f, d, p, c) 
    matterFilterData = '%s|%s||'%(chartstring, nonSponAccounts)
    fi.write(matterFilterData)

def matterFileCreate(f, d, p, c, pn, fi):

    data = '%s-%s-UMCIP-%s-1-%s|UMN01||NONSP|CPPM Project Management-%s||FALSE|||CF010|12007||eng||USD|CPPMX|||||||OnSelect1=AccountCode' %(f, d, p, c, pn) 
    fi.write(data)

while addAnother == 'y':

    fund = input("Enter Fund: ").strip()
    deptid = input('Enter Deptid: ').strip()
    project = input('Enter Project: ').strip()
    CF1 = input('Enter CF1: ').strip()
    print('Run the following SQL and enter the results:')
    query = "select project_id, descr from ps_project where project_id in ('%s') order by project_id asc" %(project)
    pyperclip.copy(query)
    print('the query %s has been added to your clipboard, ctrl+v and run in SQL' %(query))
    projectName = input('Project Name: ')
    addAnother = input('Process another? (y or n): ').lower()
    matterFileCreate(fund, deptid, project, CF1, projectName, matterFile)
    matterFilterFileCreate(fund, deptid, project, CF1, matterFilterFile)

    if addAnother == 'y':
        matterFile.write('\n')
        matterFilterFile.write('\n')

else:

    matterFile.close()
    matterFilterFile.close()
    ackMatterFile.close()
    ackFilterFile.close()
