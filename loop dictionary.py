peoples ={"Ahmed":{"HTML":"70%","CSS":"60%","JS":"90%"},
"Mostafa":{"HTML":"50%","CSS":"30%","JS":"80%"},
"Osama":{"HTML":"30%","CSS":"40%","JS":"90%"}}
# for i in peoples :
#     print(f"{i} has skills of : ")
#     for j in peoples[i] :
#         print(f"{j} => {peoples[i][j]}")
for key,value in peoples.items() :
    print(f" {key} got a skill progress : ")
    for key2,value2 in value.items():
        print(f"{key2} => {value2}")