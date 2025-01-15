from oauth2_provider.models import Application
from django.contrib.auth.models import User
from django.utils import timezone

# Crea un usuario de ejemplo (si es necesario)
#user = User.objects.create_user(username='alejandro', password='alejandro')
user = User.objects.create_superuser('facturedtest', 'facturedtest@example.com', 'facturedtest')

# Crea la aplicación OAuth2
application = Application.objects.create(
    name="Oauth factured",
    client_id="facturedtest",  # Generado automáticamente, pero se puede especificar
    client_secret="facturedtest",  # Generado automáticamente, pero se puede especificar
    client_type=Application.CLIENT_CONFIDENTIAL,  # CLIENT_PUBLIC o CLIENT_CONFIDENTIAL
    authorization_grant_type=Application.GRANT_PASSWORD,  # O Authorization Code: Application.GRANT_AUTHORIZATION_CODE
    redirect_uris="http://localhost/callback",  # Solo si usas el flujo de código de autorización
    user=user,  # Asociado a un usuario si es necesario
    skip_authorization=True,  # Opcional: si quieres omitir la autorización
)

# Imprime los datos de la aplicación creada
print(f"Application Created: {application.name}")
print(f"Client ID: {application.client_id}")
print(f"Client Secret: {application.client_secret}")