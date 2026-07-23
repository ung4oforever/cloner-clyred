import aiohttp
import asyncio
import os
import base64
import traceback
from typing import Optional, Dict, List, Any, Union

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear()
    red = '\033[91m'
    reset = '\033[0m'
    b = f"""{red}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⣀⣀⣀⣀⣀⣀⣀⠀⣰⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣟⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣟⣾⣳⢯⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣟⡾⣽⣻⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣯⣟⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣠⣤⣄⣰⣿⣿⣶⡀⢿⣿⣿⣾⣿⣿⣿⣿⡿⢿⣻⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡿⠛⠉⠉⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⠘⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠈⠛⣽⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣻⢿⡿⣧⣟⣿⠀⢸⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠘⣟⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣸⣿⣿⣷⢯⡿⣽⣳⣿⣻⣷⣾⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠘⣯⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⣰⣯⣿⡿⠀⠀⢀⣴⣾⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⣿⢿⣯⣟⣷⣿⣯⣛⣿⠿⣿⣿⣿⣿⣷⣦⣤⣤⣀⡀⠀⠀⠀⢹⣿⣿⣿⣿⡇⠀⠀⠀⢀⣴⣯⣿⡿⠃⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀
⠀⠻⣿⣿⣿⡾⣟⣿⣮⡿⣿⣹⣟⡳⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣼⣿⣿⣿⣿⣧⣤⣶⣾⣿⣿⣿⣿⣿⡇⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀
⠀⠀⠀⠉⠙⢿⣿⣛⣷⣻⡾⣟⠾⣽⡹⣞⡽⣿⣿⣟⡿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⡿⣟⣾⣯⡀⠀⠀⠀⠉⠛⠉⠙⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢻⣷⣟⣯⢷⣛⣞⢯⣳⢏⣷⢫⣗⢯⣟⣿⣼⣳⢏⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⢿⣟⣿⣿⣦⡀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢩⠿⢿⣞⡽⢮⣻⣵⣻⢎⡿⣼⢫⣞⢾⣹⢿⣫⢷⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⡾⣽⣻⣞⣿⣿⣽⣿⣦⡀⠀⠀⠀⠀⣿⣿⣿⣿⡿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⠁⠀⠀⠙⢿⣿⢯⡗⣯⢏⣷⢫⣟⡼⣏⣾⢻⣯⢟⣿⢿⣽⣿⣿⣿⣿⣿⣿⡾⣿⢯⣷⣻⢾⣽⣷⣯⣟⣿⣷⣄⡀⣸⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠰⠁⠀⠀⠀⡠⠉⢻⣿⣞⣭⡟⣮⢟⣼⣳⢻⣼⣿⣛⣾⣟⣿⣿⣿⣿⡿⣿⣟⣿⣿⣽⣿⣳⣯⣟⣾⣻⣿⣞⡷⣯⢿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠆⠀⠀⠀⡐⠁⠀⠀⠙⣷⣧⢿⣹⡞⣧⢯⣿⡟⣾⣱⣾⣟⣿⣿⣿⣿⣽⣳⣟⣾⣿⣷⣻⣿⢾⡽⣞⡷⣿⣿⣽⣯⣟⡾⣽⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠸⠀⠀⠀⢰⠀⠀⠀⠀⠀⢸⣿⡿⣶⢿⡿⣻⢧⢿⣱⢯⣿⣾⣿⢾⣿⣟⣾⣷⣿⣿⣻⣿⢷⣻⣿⡽⣯⣟⣷⣻⢿⣷⣯⣟⣷⣿⣿⣿⣿⣇⡀⠀⠀⠀
⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡯⢷⣫⣟⣼⢳⢯⣳⢏⣿⡷⣿⣿⣿⣾⣽⣻⣿⣽⣾⣷⣿⣿⢯⣿⣟⣷⣻⢾⡽⣯⣿⣻⣿⣾⣿⣿⣿⣿⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⢫⣽⢳⣳⢮⣳⢯⣻⢼⡻⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡾⣽⢯⣟⣷⣿⣿⣿⣿⣿⣿⠿⢿⣟⡁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣯⡿⣜⣯⢳⣏⢷⡻⣼⢳⣻⣽⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⡿⠈⠙⢉⣴⣿⡿⣿⣷⣄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⣽⣮⣿⣼⣯⣷⣯⣯⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣿⣿⡿⣽⣳⣿⣿⡗
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣟⣮⣳⣟⣶⣫⣷⣳⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⡿⣽⣿⣻⣷⠟⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣾⣿⣿⣿⡟⣿⣿⢻⣽⣿⢳⣿⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⢿⣻⣿⣽⣷⣿⣿⣿⠟⠋⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣯⣟⡷⣯⣿⢿⣽⡿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠉⠛⠿⠿⢿⣿⡿⣾⣽⣻⣿⣽⣿⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣯⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⢷⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⢿⣽⣻⢿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣯⣿⡾⠿⠿⢿⣯⢿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣻⣿⢿⣷⣷⣷⣶⣦⣾⣽⣻⡇⠀⠀dev: zay (6cbj) - discord.gg/clyred⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣳⢿⣻⣟⣾⢿⡽⣯⢷⣯⣿⠇ server clone⠀tool⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣷⣿⣾⡿⣿⣿⣿⣿⠏⠀⠀
{reset}"""
    print(b)

class ClyredAPIError(Exception):
    def __init__(self, status: int, endpoint: str, message: str):
        self.status = status
        self.endpoint = endpoint
        self.message = message
        super().__init__(f"CLYRED_HTTP_{status} | {endpoint} | {message}")

class ClyredCloneServer:
    def __init__(self, token: str, src: str, tgt: str):
        self.token = token
        self.src = src
        self.tgt = tgt
        self.clyred_headers = {"authorization": token}
        self.clyred_json_headers = {"authorization": token, "content-type": "application/json"}
        self.clyred_session: Optional[aiohttp.ClientSession] = None

    async def __aenter__(self):
        connector = aiohttp.TCPConnector(limit=50)
        self.clyred_session = aiohttp.ClientSession(connector=connector)
        return self

    async def __aexit__(self, *args):
        if self.clyred_session:
            await self.clyred_session.close()

    async def clyred_api_call(
        self,
        method: str,
        endpoint: str,
        data: Union[Dict, List, None] = None,
        use_json: bool = True
    ) -> Union[Dict, List, None]:
        url = f"https://discord.com/api/v10{endpoint}"
        headers = self.clyred_json_headers if use_json else self.clyred_headers
        
        for attempt in range(5):
            try:
                kwargs = {"headers": headers, "timeout": aiohttp.ClientTimeout(total=10)}
                if use_json and data is not None:
                    kwargs["json"] = data
                elif not use_json and data is not None:
                    kwargs["data"] = data
                
                async with self.clyred_session.request(method, url, **kwargs) as response:
                    if response.status in (200, 201, 204):
                        if response.status == 204:
                            return {}
                        try:
                            return await response.json()
                        except aiohttp.ContentTypeError:
                            return {}
                    
                    if response.status == 429:
                        retry_after = float(response.headers.get("retry-after", 1))
                        await asyncio.sleep(retry_after)
                        continue
                    
                    error_text = await response.text()
                    raise ClyredAPIError(response.status, endpoint, error_text[:200])
            
            except ClyredAPIError:
                raise
            except aiohttp.ClientError as e:
                if attempt == 4:
                    raise ClyredAPIError(0, endpoint, str(e))
                await asyncio.sleep(min(0.5 * (2 ** attempt), 5))
        
        return None

    async def clyred_fetch_guild(self, guild_id: str) -> Optional[Dict]:
        return await self.clyred_api_call("get", f"/guilds/{guild_id}")

    async def clyred_fetch_channels(self, guild_id: str) -> List[Dict]:
        return await self.clyred_api_call("get", f"/guilds/{guild_id}/channels") or []

    async def clyred_fetch_roles(self, guild_id: str) -> List[Dict]:
        return await self.clyred_api_call("get", f"/guilds/{guild_id}/roles") or []

    async def clyred_fetch_emojis(self, guild_id: str) -> List[Dict]:
        return await self.clyred_api_call("get", f"/guilds/{guild_id}/emojis") or []

    async def clyred_fetch_stickers(self, guild_id: str) -> List[Dict]:
        return await self.clyred_api_call("get", f"/guilds/{guild_id}/stickers") or []

    async def clyred_nuke_channels(self) -> None:
        channels = await self.clyred_fetch_channels(self.tgt)
        tasks = [self.clyred_api_call("delete", f"/channels/{c['id']}") for c in channels]
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
            await asyncio.sleep(1)

    async def clyred_nuke_roles(self) -> None:
        roles = await self.clyred_fetch_roles(self.tgt)
        tasks = []
        for r in roles:
            if r["id"] != self.tgt and not r.get("managed"):
                tasks.append(self.clyred_api_call("delete", f"/guilds/{self.tgt}/roles/{r['id']}"))
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
            await asyncio.sleep(1)

    async def clyred_nuke_emojis_stickers(self) -> None:
        emojis = await self.clyred_fetch_emojis(self.tgt)
        stickers = await self.clyred_fetch_stickers(self.tgt)
        tasks = []
        for e in emojis:
            tasks.append(self.clyred_api_call("delete", f"/guilds/{self.tgt}/emojis/{e['id']}"))
        for s in stickers:
            tasks.append(self.clyred_api_call("delete", f"/guilds/{self.tgt}/stickers/{s['id']}"))
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)

    async def clyred_update_guild_config(self, src_guild: Dict) -> Dict[str, str]:
        clyred_channel_map = {}
        
        clyred_settings = {}
        if src_guild.get("name"):
            clyred_settings["name"] = src_guild["name"]
        if src_guild.get("description") is not None:
            clyred_settings["description"] = src_guild.get("description", "")
        if src_guild.get("preferred_locale"):
            clyred_settings["preferred_locale"] = src_guild["preferred_locale"]
        if src_guild.get("verification_level") is not None:
            clyred_settings["verification_level"] = src_guild["verification_level"]
        if src_guild.get("explicit_content_filter") is not None:
            clyred_settings["explicit_content_filter"] = src_guild["explicit_content_filter"]
        if src_guild.get("default_message_notifications") is not None:
            clyred_settings["default_message_notifications"] = src_guild["default_message_notifications"]
        if src_guild.get("afk_timeout") is not None:
            clyred_settings["afk_timeout"] = src_guild["afk_timeout"]
        if src_guild.get("premium_progress_bar_enabled") is not None:
            clyred_settings["premium_progress_bar_enabled"] = src_guild["premium_progress_bar_enabled"]

        if clyred_settings:
            await self.clyred_api_call("patch", f"/guilds/{self.tgt}", clyred_settings)
        
        return clyred_channel_map

    async def clyred_clone_icon(self, src_guild: Dict) -> None:
        if not src_guild.get("icon"):
            return
        
        try:
            async with self.clyred_session.get(
                f"https://cdn.discordapp.com/icons/{self.src}/{src_guild['icon']}.png?size=256",
                timeout=aiohttp.ClientTimeout(total=10)
            ) as r:
                if r.status == 200:
                    clyred_icon_bytes = await r.read()
                    clyred_icon_b64 = base64.b64encode(clyred_icon_bytes).decode('utf-8')
                    await self.clyred_api_call(
                        "patch",
                        f"/guilds/{self.tgt}",
                        {"icon": f"data:image/png;base64,{clyred_icon_b64}"}
                    )
        except aiohttp.ClientError:
            pass

    async def clyred_clone_roles(self) -> Dict[str, str]:
        clyred_src_roles = await self.clyred_fetch_roles(self.src)
        clyred_filtered_roles = [r for r in clyred_src_roles if r["id"] != self.src and not r.get("managed")]
        clyred_sorted_roles = sorted(clyred_filtered_roles, key=lambda x: x.get("position", 0), reverse=True)
        
        clyred_role_map = {}
        
        for clyred_role in clyred_sorted_roles:
            clyred_role_data = {
                "name": clyred_role.get("name", "new role"),
                "color": clyred_role.get("color", 0),
                "hoist": clyred_role.get("hoist", False),
                "mentionable": clyred_role.get("mentionable", False),
                "permissions": str(clyred_role.get("permissions", 0)),
            }
            
            if clyred_role.get("unicode_emoji"):
                clyred_role_data["unicode_emoji"] = clyred_role["unicode_emoji"]
            
            clyred_new_role = await self.clyred_api_call("post", f"/guilds/{self.tgt}/roles", clyred_role_data)
            if clyred_new_role and "id" in clyred_new_role:
                clyred_role_map[clyred_role["id"]] = clyred_new_role["id"]
            await asyncio.sleep(0.2)
        
        return clyred_role_map

    async def clyred_reorder_roles(self, clyred_role_map: Dict[str, str]) -> None:
        if not clyred_role_map:
            return
        
        clyred_src_roles = await self.clyred_fetch_roles(self.src)
        clyred_role_positions = []
        
        for clyred_old_id, clyred_new_id in clyred_role_map.items():
            clyred_original_role = next((r for r in clyred_src_roles if r["id"] == clyred_old_id), None)
            if clyred_original_role and "position" in clyred_original_role:
                clyred_role_positions.append({
                    "id": clyred_new_id,
                    "position": clyred_original_role["position"]
                })
        
        if clyred_role_positions:
            await self.clyred_api_call("patch", f"/guilds/{self.tgt}/roles", clyred_role_positions)

    def clyred_build_overwrites(self, clyred_old_overwrites: List[Dict], clyred_role_map: Dict[str, str]) -> List[Dict]:
        if not clyred_old_overwrites:
            return []
        
        clyred_new_overwrites = []
        for clyred_overwrite in clyred_old_overwrites:
            clyred_old_id = clyred_overwrite.get("id")
            clyred_new_id = clyred_role_map.get(clyred_old_id, clyred_old_id)
            
            if clyred_old_id == self.src:
                clyred_new_id = self.tgt
            
            clyred_new_overwrites.append({
                "id": clyred_new_id,
                "type": clyred_overwrite.get("type", 0),
                "allow": clyred_overwrite.get("allow", "0"),
                "deny": clyred_overwrite.get("deny", "0")
            })
        
        return clyred_new_overwrites

    async def clyred_clone_channels(self, clyred_role_map: Dict[str, str]) -> Dict[str, str]:
        clyred_src_channels = await self.clyred_fetch_channels(self.src)
        
        valid_types = {0, 2, 4, 5, 13, 15}
        
        clyred_categories = sorted(
            [c for c in clyred_src_channels if c["type"] == 4],
            key=lambda x: x.get("position", 0)
        )
        clyred_other_channels = sorted(
            [c for c in clyred_src_channels if c["type"] != 4 and c["type"] in valid_types],
            key=lambda x: x.get("position", 0)
        )
        
        clyred_parent_map = {}
        
        for clyred_cat in clyred_categories:
            clyred_overwrites = self.clyred_build_overwrites(clyred_cat.get("permission_overwrites", []), clyred_role_map)
            clyred_new_cat = await self.clyred_api_call("post", f"/guilds/{self.tgt}/channels", {
                "name": clyred_cat.get("name", "category"),
                "type": 4,
                "permission_overwrites": clyred_overwrites
            })
            if clyred_new_cat and "id" in clyred_new_cat:
                clyred_parent_map[clyred_cat["id"]] = clyred_new_cat["id"]
            await asyncio.sleep(0.15)
        
        for clyred_ch in clyred_other_channels:
            clyred_parent_id = clyred_parent_map.get(clyred_ch.get("parent_id"))
            clyred_overwrites = self.clyred_build_overwrites(clyred_ch.get("permission_overwrites", []), clyred_role_map)
            
            clyred_channel_data = {
                "name": clyred_ch.get("name", "channel"),
                "type": clyred_ch.get("type", 0),
                "parent_id": clyred_parent_id,
                "permission_overwrites": clyred_overwrites,
            }
            
            if clyred_ch["type"] in (0, 5, 13, 15):
                clyred_channel_data["topic"] = clyred_ch.get("topic", "")
                clyred_channel_data["nsfw"] = clyred_ch.get("nsfw", False)
                clyred_channel_data["rate_limit_per_user"] = clyred_ch.get("rate_limit_per_user", 0)
            elif clyred_ch["type"] == 2:
                clyred_channel_data["bitrate"] = clyred_ch.get("bitrate", 64000)
                clyred_channel_data["user_limit"] = clyred_ch.get("user_limit", 0)
            
            if clyred_ch["type"] == 15:
                clyred_channel_data["available_tags"] = clyred_ch.get("available_tags", [])
                clyred_channel_data["default_reaction_emoji"] = clyred_ch.get("default_reaction_emoji")
            
            clyred_channel_data = {k: v for k, v in clyred_channel_data.items() if v is not None}
            
            await self.clyred_api_call("post", f"/guilds/{self.tgt}/channels", clyred_channel_data)
            await asyncio.sleep(0.15)
        
        return clyred_parent_map

    async def clyred_clone_emojis(self) -> None:
        clyred_src_emojis = await self.clyred_fetch_emojis(self.src)
        if not clyred_src_emojis:
            return
        
        for clyred_emoji in clyred_src_emojis:
            try:
                clyred_ext = "gif" if clyred_emoji.get("animated") else "png"
                async with self.clyred_session.get(
                    f"https://cdn.discordapp.com/emojis/{clyred_emoji['id']}.{clyred_ext}?size=128",
                    timeout=aiohttp.ClientTimeout(total=10)
                ) as r:
                    if r.status == 200:
                        clyred_emoji_bytes = await r.read()
                        clyred_emoji_b64 = base64.b64encode(clyred_emoji_bytes).decode('utf-8')
                        
                        await self.clyred_api_call("post", f"/guilds/{self.tgt}/emojis", {
                            "name": clyred_emoji["name"],
                            "image": f"data:image/{clyred_ext};base64,{clyred_emoji_b64}"
                        })
                        await asyncio.sleep(0.3)
            except aiohttp.ClientError:
                pass

    async def clyred_sync_channel_refs(self, clyred_channel_map: Dict[str, str]) -> None:
        clyred_src_guild = await self.clyred_fetch_guild(self.src)
        if not clyred_src_guild:
            return
        
        clyred_settings = {}
        for clyred_setting_name in ["afk_channel_id", "system_channel_id", "rules_channel_id", "public_updates_channel_id"]:
            clyred_old_id = clyred_src_guild.get(clyred_setting_name)
            if clyred_old_id and clyred_old_id in clyred_channel_map:
                clyred_settings[clyred_setting_name] = clyred_channel_map[clyred_old_id]
        
        if clyred_settings:
            await self.clyred_api_call("patch", f"/guilds/{self.tgt}", clyred_settings)

    async def clyred_create_white_role(self) -> None:
        clyred_me = await self.clyred_api_call("get", "/users/@me")
        if clyred_me and "id" in clyred_me:
            clyred_white_role = await self.clyred_api_call("post", f"/guilds/{self.tgt}/roles", {
                "name": "clyred.white",
                "color": 16777215,
                "hoist": False,
                "mentionable": False,
                "permissions": "0"
            })
            
            if clyred_white_role and "id" in clyred_white_role:
                await self.clyred_api_call(
                    "put",
                    f"/guilds/{self.tgt}/members/{clyred_me['id']}/roles/{clyred_white_role['id']}"
                )

    async def clyred_clone_server(self) -> None:
        try:
            clyred_src_guild = await self.clyred_fetch_guild(self.src)
            if not clyred_src_guild:
                print("\033[91msource guild not found\033[0m")
                return

            await self.clyred_nuke_channels()
            await self.clyred_nuke_roles()
            await self.clyred_nuke_emojis_stickers()
            await asyncio.sleep(2)

            await self.clyred_clone_icon(clyred_src_guild)
            clyred_channel_map = await self.clyred_update_guild_config(clyred_src_guild)

            clyred_role_map = await self.clyred_clone_roles()
            if clyred_role_map:
                await self.clyred_reorder_roles(clyred_role_map)

            clyred_new_parent_map = await self.clyred_clone_channels(clyred_role_map)
            clyred_channel_map.update(clyred_new_parent_map)
            
            await self.clyred_sync_channel_refs(clyred_channel_map)
            await self.clyred_clone_emojis()
            await self.clyred_create_white_role()

            print("\033[92mclone completed successfully\033[0m")
        
        except ClyredAPIError as e:
            print(f"\033[91m{e}\033[0m")
        except Exception as e:
            print(f"\033[91m{type(e).__name__}: {e}\033[0m")

async def main():
    try:
        banner()
        token = input("\033[96mtoken: \033[0m").strip()
        src = input("\033[96msource server id: \033[0m").strip()
        tgt = input("\033[96mtarget server id: \033[0m").strip()
        
        if not all([token, src, tgt]):
            print("\033[91mall fields are required\033[0m")
            return
        
        async with ClyredCloneServer(token, src, tgt) as clyred:
            await clyred.clyred_clone_server()
    except Exception as e:
        print(f"\033[91m{type(e).__name__}: {e}\033[0m")

if __name__ == "__main__":
    asyncio.run(main())
