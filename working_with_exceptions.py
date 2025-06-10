# Things can go wrong in code, and Python will try 
# to handle run-time problems using 'exception' types





if __name__ == '__main__':
    try:
        # here we deliberately raise an exception
        broken = int('three')
    except ValueError as ve: # code for specific problems
        print(f'Value Error: {ve}')
    except Exception as err: # ...catch any remaining problems
        print(f'there was a problem: {err}')
    finally: # this is optional
        print('this block will run even if there is a problem')