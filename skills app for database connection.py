import sqlite3

my_db = sqlite3.connect(r'C:\Users\mhbk8\Documents\Python\app.db')  
cr = my_db.cursor()

cr.execute("CREATE TABLE if not exists skills (skill_name text,progress integer,user_id integer)") 
def save_close_app():
    my_db.commit()
    my_db.close()
    print('you saved changes and closed the app ') 
user_id = int(input("which user are you ? 1 or 2 or 3 : "))    
  
input_message = '''what do you want to do ?
s => show your skills
a => add a skill
d => delete a skill
u => update a skill
q => quit the app
choose an option : 
'''
user_input = input(input_message).strip().lower()
command_list = ['s','a','d','u','q']
while user_input not in command_list :
    print("please enter a right option")
    user_input = input(input_message).strip().lower()
def show_skills() :
    cr.execute(f"select * from SKILLS where user_id = '{user_id}' ")
    results = cr.fetchall()
    print(f"you have {len(results)} skills")
    if len(results) > 0 :
             print("showing the skills : ")
    for i in results :
        print(f"skill => {i[0]} ",end=' ')
        print(f"progress => {i[1]}% ")

    save_close_app()
      
def add_skills() :
    my_skill = input("enter your skill : ").strip().upper()
    cr.execute(f"select skill_name from SKILLS where user_id = '{user_id}'and skill_name ='{my_skill}' ")
    results = cr.fetchone()
    if results == None :
        print("you can add this skill ")
        my_progress = int(input("enter your progress : ").strip())
        cr.execute(f"insert into skills(skill_name,progress,user_id) values('{my_skill}','{my_progress}','{user_id}') ")
    else :
        possib =input("This skill is already exist Do you want to update it? \n Enter y or n : " )
        if possib == 'y':
               my_progress = int(input("enter the updated progress : ").strip())
               cr.execute(f"update skills set progress = {my_progress} where user_id = {user_id} and skill_name = '{my_skill}'  ")
        else :
            pass      
    
    
    save_close_app()
     
def delete_skills() :
    my_skill = input("enter the skill that you want to delete : ").strip().upper()
    cr.execute(f"delete from skills where skill_name = '{my_skill}' and user_id = '{user_id}'  ")
    save_close_app()
def update_skills() :
    my_skill = input("enter the skill that you want to update : ").strip().upper()
    my_progress = int(input("enter the updated progress : ").strip())
    cr.execute(f"update skills set progress = {my_progress} where user_id = {user_id} and skill_name = '{my_skill}'  ")
    save_close_app()

if user_input =='s' :
    show_skills()
elif user_input == 'a' :
    add_skills()
elif user_input == 'd' :
    delete_skills()        
elif user_input == 'u' :
    update_skills()      
else :
    save_close_app()