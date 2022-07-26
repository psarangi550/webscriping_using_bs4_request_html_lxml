import click #importing the click module 

@click.command() #initializing the click module
#here asing the user to put the username and password
@click.option("--user","-u",prompt=True)
@click.option("--password","-p",prompt=True,hide_input=True,confirmation_prompt=True)

#defining the function for the same 
def login(user,password):
    click.echo("username is {user} and password is {password}".format(user=user, password=password))

#alternate approach
user_name=None
passwd=None
def alter_login():
    user_name=click.prompt("username")
    passwd=click.prompt("Enter password",hide_input=True,confirmation_prompt=True)
    click.echo("username is {user} and password is {password}".format(user=user_name, password=passwd))

if __name__ == "__main__":
    # login() #calling the login function woth out args as those will be provided from the cmdline
    alter_login()

