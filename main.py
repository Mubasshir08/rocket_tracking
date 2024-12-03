# Today we will track our rocket 🚀
# We will take some info about rocket from user and use those to track out rocket 🎉🎉

# Rocket tracking formula 👇

# 🏹 Higest height 👉 H = (pre_velocity ** 2) * sin**2{deg} / 2 * gravity
# 📐 Horizontal lenght 👉 L = (pre_velocity ** 2) * sin{2 * deg} / gravity
# 🛫 Time of fly 👉 T = 2 * pre_velocity * sin{deg} / gravity
# 📍  Exact timing location 👇
        # Horizontally 👉 Hx = ( pre_velocity * cos{deg} ) * time
        # Vertically   👉 Vy = (( pre_velocity * sin{deg} ) * time) - (0.5 * gravity * (time ** 2))

# Taking info from user

rocket_name = input('Please enter your rocket name : \n')
isLunch =  input('Do you want to lunch it 🚀? \n').lower()
gravity = 0

if isLunch == 'yes':
    pre_velocity = float(input('Velocity (ms^-2) : '))
    lunch_degree = float(input('lunch_degree : '))
    isGravityDefault = input('Do you want to keep gravity value default ? \n').lower()

    if isGravityDefault == 'yes' :
        gravity = 9.8
    elif isGravityDefault == 'no' :
        gravity = input('Please give the gravity value ? \n')
    else:
        print('wrong input')
        gravity = input('Please give the gravity value ? \n')

elif isLunch == 'no':
    print('Thanks For Coming !')
else:
    print('wrong input')
    







