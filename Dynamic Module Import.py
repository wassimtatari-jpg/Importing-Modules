module_name=input("enter moudle name :")
function_name=input("Enter funcation name : ")

module=__import__(module_name)

function=getattr(module,function_name)

function(15)