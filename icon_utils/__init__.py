from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider

provider = "https://ctz.solidwallet.io"

# Creates an IconService instance using the HTTP provider and set a provider.
icon_service = IconService(HTTPProvider(provider, 3))

balanced_dex = "cxa0af3165c08318e988cb30993b3048335b94af6c"