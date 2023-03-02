from Usuarios.models import Usuarios

def validarSession(request):
    nombre = request.session.get('nombre')
    if nombre is None:
        return False
    return True

def validarCorreo(request):#Verifica si el correo ya esta registrado en la base de datos
    usuarios = Usuarios.objects.all()
    mailUsuario = request.POST['email']
    correo = ''

    for usuario in usuarios:
        correo = usuario.correoUsuarios
        if correo == mailUsuario:
            return True
        
    return False

def validarNombre(request):#Verifica si el nombre ya esta registrado en la base de datos
    usuarios = Usuarios.objects.all()
    nombreUsuario = request.POST['nombre']
    nombre = ''

    for Usuario in usuarios:
        nombre = Usuario.nombreUsuarios
        if nombre == nombreUsuario:
            return True

    return False

def validarPass(request):#Verifica si el nombre ya esta registrado en la base de datos

    passwordIngresado = request.POST['password']
    usuarios = Usuarios.objects.get(correoUsuarios = request.POST['email'])
    passwordEncontrado = usuarios.passwordUsuarios

    if passwordIngresado == passwordEncontrado:
        return True
    else:
        return False
    

def insertarUsuarios(request):#inserta a los usuarios en la base de datos
    nombre = request.POST['nombre']
    mail = request.POST['email']
    password = request.POST['password']

    try:
        Usuarios.objects.create(nombreUsuarios=nombre, correoUsuarios=mail, passwordUsuarios=password)
    except Exception as e:
        print("Error inserting")
    