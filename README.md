# Proyecto-social
# PRIMERA PARTE:
Vamos a generar de forma automática la documentación de un proyecto de interés social, hecho en Django. Para ello:

1. Hacemos grupos (ya está hecho)
2. Usamos Jira con VisualStudio y github.
3. Comenzamos a programar sin olvidarnos de los famosos commits, obviamente en Django.
4. Generamos la documentación de forma automática. Siempre usando Despliegue continuo.
5. Y por no complicarnos la vida que estamos empezando y ya haremos más historias hacemos un despliegue en github pages o similar.

# SEGUNDA PARTE:
Utilizar GithubActions para, a través de terraform tener una instancia con un contenedor que despliegue Jenkins.

Utilizamos:

1. Integración y despliegue continuo (GithubActions).
2. Terraform.
3. Docker.
4. Jenkins.



# GUÍA
La aplicación se basa en la creación de tests psicológicos de autoevaluación. 
Estos se pueden crear, se les pueden añadir preguntas, eliminar las mismas e incluso editarlas siempre y cuando el usuario registrado sea mayor de edad. En caso contrario, el usuario podrá ver el test con sus respectivas preguntas (de momento no puede responderlo, se implementará en el futuro).

ESTÁ HECHO ÚNICAMENTE EN DJANGO, framework de PHP.

- tests_app: App de Python para trabajar todo lo relacionado con los tests
- usuarios_app: App de Python para trabajar todo lo relacionado con el inicio de sesión (mediante el token que usa Django por defecto)
- db.sqlite3: BD que usa Django por defecto, en la cual se encuentran los modelos 
- Modelos: Solo hay 3 -> Usuario, Test y Pregunta || Un usuario puede tener varios test, un test es de un usuario, una pregunta puede ser de un solo test y un test puede tener varias preguntas