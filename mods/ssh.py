import paramiko
from mods.say import say
from mods.listen import listen

def ssh(available_SSH): #Clean Up: Find Better Method
    availablePi = []

    say("Would you like me to tell you your SSH Options?")
    while True:
        try:
            recognized_Audio = "NO"
            if "YES" in recognized_Audio:
                for each in available_SSH.items():
                    say("For Pi {0}, the IP Address is {1}".format(each[0],each[1][0]))
                    print(each[0],each[1])

                break
            if "NO" in recognized_Audio:
                say("Alright")
                break

        except Exception as e:
            print(e)
            say("NOTHING")
            continue


    say("Which Pi would you like to SSH in to?")
    while True:
        try:
            recognized_Audio = "1"
            if "ONE" in recognized_Audio:
                recognized_Audio = "1"

            if recognized_Audio in available_SSH:
                say("Going to Log in to Pi " + recognized_Audio)
                print(available_SSH[recognized_Audio])
                ADDRESS = available_SSH[recognized_Audio][0]
                USERNAME = available_SSH[recognized_Audio][1]
                PASSWORD = available_SSH[recognized_Audio][2]

                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(ADDRESS, username=USERNAME, password=PASSWORD)
                stdin,stdout,stderr = ssh.exec_command("ls")
                output = stdout.readlines()
                print(len(output))
                say("There are {0} entries in the Home Folder.".format(len(output)))
                say("DONE")
                break

            elif recognized_Audio not in available_SSH:
                say("This is not a valid number.")
                print(recognized_Audio)
                print(available_SSH)
                continue

        except paramiko.ssh_exception.NoValidConnectionsError as e:
            say("Could not make the connection. SSH may not be enabled on the remote machine.")
            say("Would you like to try again?")
            recognized_Audio = listen()
            if "YES" in recognized_Audio:
                say("Retrying")
                continue
            if "NO" in recognized_Audio:
                say("Okay")
                break

        except paramiko.ssh_exception.AuthenticationException as e:
            say("There was an Authentication Error. You may want to go back to the CSV file and make the required changes.")
            break

        except Exception as e:
            print(e)
            say("NOTHING")
            continue
