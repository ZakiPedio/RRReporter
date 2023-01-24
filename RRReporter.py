

def banner():
    print("""


        ██████╗ ██████╗ ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗███████╗██████╗ 
        ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
        ██████╔╝██████╔╝██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   █████╗  ██████╔╝
        ██╔══██╗██╔══██╗██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══╝  ██╔══██╗
        ██║  ██║██║  ██║██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   ███████╗██║  ██║
        ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                    Rapid Rabbit Reporter

    """)

def selectVuln():
    answer = ""
    while (answer != r"^[0-9]$"):
        print("""
           <===============RRReporter===============>
            0. > Cross Site Scripting        [XSS]
            1. > SQL Injection               [SQLI]
            2. > Server-Side Request Forgery [SSRF]
            3. > Unrestricted File Upload    [UFU]
            4. > Local File Inclusion        [LFI]
            5. > Remote File Inclusion       [RFI]
            6. > JSON Web Token              [JWT]
           <========================================>
        https://github.com/swisskyrepo/PayloadsAllTheThings
             """)
            # https://github.com/swisskyrepo/PayloadsAllTheThings
            # https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection
            # https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/NoSQL%20Injection
            # https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Request%20Forgery
            # https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Upload%20Insecure%20Files
            # https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/File%20Inclusion https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Directory%20Traversal
            #
            # https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/JSON%20Web%20Token
        
        try:
            answer = int(input("RRReporter> "))
        except:
            continue

        if answer == 0:
            print("Cross Site Scripting")
            return answer
        elif answer == 1:
            print("SQL Injection")
            return answer
        elif answer == 2:
            print("Server-Side Request Forgery")
            return answer
        elif answer == 3:
            print("Unrestricted File Upload")
            return answer
        elif answer == 4:
            print("Local File Inclusion")
            return answer
        elif answer == 5:
            print("Remote File Inclusion")
            return answer
        elif answer == 6:
            print("JSON Web Token")
            return answer


def specificType(vulnCode):
    answer = ""
    if vulnCode == 0:
        while (answer != r"^[0-2]$"):
            print("""
           <===============RRReporter===============>
            Which type of XSS vulnerability?

            0. > Reflected XSS
            1. > Stored XSS
            2. > DOM Based XSS
           <========================================>

            """)
            try:
                answer = int(input("RRReporter> "))
            except:
                continue
            if answer == 0:
                return "Reflected"
            elif answer == 1:
                return "Stored"
            elif answer == 2:
                return "DOM Based"
    elif vulnCode == 1:
        while (answer != r"^[0-4]$"):
            print("""
           <===============RRReporter===============>
            Which type of SQLi vulnerability?

            0. > Logic SQLi
            1. > Union SQLi
            2. > Blind SQLi
            3. > Time-Based SQLi
            4. > NoSQLi
           <========================================>

            """)
            try:
                answer = int(input("RRReporter> "))
            except:
                continue
            if answer == 0:
                return "Logic"
            elif answer == 1:
                return "Union"
            elif answer == 2:
                return "Blind"
            elif answer == 3:
                return "Time-Based"
            elif answer == 4:
                return "NoSQL"
    elif vulnCode == 2:
        while (answer != r"^[0-2]$"):
            print("""
           <===============RRReporter===============>
            Which type of SSRF vulnerability?

            0. > Blind SSRF
            1. > Semi-Blind SSRF
            2. > Non-Blind SSRF
           <========================================>

            """)
            try:
                answer = int(input("RRReporter> "))
            except:
                continue
            if answer == 0:
                return "Blind"
            elif answer == 1:
                return "Semi-Blind"
            elif answer == 2:
                return "Non-Blind"
    elif vulnCode == 3:
        while (answer != r"^[0-2]$"):
            print("""
           <===============RRReporter===============>
            Which type of UFU vulnerability?

            0. > Extension-Based UFU
            1. > Magic-Bytes UFU
            2. > CVE-Based UFU
           <========================================>

            """)
            try:
                answer = int(input("RRReporter> "))
            except:
                continue
            if answer == 0:
                return "Blind"
            elif answer == 1:
                return "Magic-Bytes"
            elif answer == 2:
                return "CVE-Based"
    elif vulnCode == 4 or vulnCode == 5:
         while (answer != r"^[0-1]$"):
            print("""
           <===============RRReporter===============>
            Which type of LFI/RFI vulnerability?

            0. > Basic LFI/RFI
            1. > PHP Wrapper LFI/RFI
           <========================================>

            """)
            try:
                answer = int(input("RRReporter> "))
            except:
                continue
            if answer == 0:
                return "Basic"
            elif answer == 1:
                return "PHP Wrapper"
    elif vulnCode == 6:
        while (answer != r"^[0-2]$"):
            print("""
           <===============RRReporter===============>
            Which type of JWT vulnerability?

            0. > Secret Brute-Force JWT
            1. > Header Parameter Injections JWT
            2. > Self-Signed JWT
           <========================================>

            """)
            try:
                answer = int(input("RRReporter> "))
            except:
                continue
            if answer == 0:
                return "Secret Brute-Force"
            elif answer == 1:
                return "Header Parameter Injections"
            elif answer == 2:
                return "Self-Signed"



def askURL():
    answer = ""
    while (answer == ""):
            print("""
           <================RRReporter================>
            In which URL you found the vulnerability?
           <==========================================>

            """)
            try:
                answer = str(input("RRReporter> "))
            except:
                continue
    return answer


def askPayload():
    answer = ""
    while (answer == ""):
            print("""
           <===============RRReporter===============>
            To which payload is the site vulnerable?
           <========================================>

            """)
            try:
                answer = str(input("RRReporter> "))
            except:
                continue
    return answer



if __name__ == "__main__":

    vulnerabilities = ["Cross-Site Scripting (XSS)", "SQL Injection (SQLi)", "Server-Side Request Forgery (SSRF)", "Unrestricted File Upload (UFU)", "Local File Inclusion (LFI)", "Remote File Inclusion (RFI)", "JSON Web Token (JWT)"]
    vShort = ["XSS", "SQLi", "SSRF", "UFU", "LFI", "RFI", "JWT"]
    # show banner
    banner()
    # ask for vulnerability type
    vulnID = selectVuln()

    # ask for specific type of vulnerability
    sVulnType = specificType(vulnID)

    # ask for the URL
    url = askURL()
    try:
        domain = url.split("/")
        domain = domain[2]
    except:
        print("ERR. Invalid url, exiting")
        exit(0)

    # ask for payload
    payload = askPayload()
    
    #debug
    print(f"\nSite: {domain}\nVulnerability type: {sVulnType} {vulnerabilities[vulnID]}\nVulnerable URL: {url}\nPayload: {payload}")

    # read and write template report
    templateReport = open("reports_template/report_template_"+ vShort[vulnID]+".txt","r")
    finalReport = open("reports/report_"+domain+"_"+vShort[vulnID]+".txt","w")
    templateReportLines = templateReport.readlines()
    templateReport.close()
    for line in templateReportLines:
        wLine = line.replace("<SVULNTYPE>",sVulnType)
        wLine = wLine.replace("<VULNERABILITY>",vulnerabilities[vulnID])
        wLine = wLine.replace("<DOMAIN>",domain)
        wLine = wLine.replace("<URL>",url)
        wLine = wLine.replace("<PAYLOAD>",payload)
        finalReport.write(wLine)
    finalReport.close()