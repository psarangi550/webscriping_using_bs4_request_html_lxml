import click #importing the click module 

#THIS WILL HELP IN CREATING THE --HELP ON PYTHON SCRIPT
@click.command()
#here we are providing the positional argument
#as the nargs=-1 , it will eat up all the value and can accept infinity number of args 
@click.argument('names',nargs=-1)

def main(names):#creating the function where the args value will be provided by the click which it accept from user
    #iterating over each argument value
    for name  in names:
        click.echo(name)

#if called directly then
if __name__ == '__main__':
    main()