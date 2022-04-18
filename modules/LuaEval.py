"""Evaluate Lua code"""
# Author: 
# Original code for evaluating C: @dzhingme_vangchuk (@h3xcode)
# Remade for lua by @Aqendo

import logging
import os
import subprocess
from .. import loader, utils
logger = logging.getLogger(__name__)


@loader.tds
class LuaEvalMod(loader.Module):
    """Evaluate Lua code"""
    strings = {"name": "LuaEval",
               "success": "Success!",
               "result": "**Evaluating :**\n\
```{prog}```\n**Interpreter output :**\n\
```{compilation}```"}

    async def client_ready(self, client, db):
        self.client = client
        self.db = db

    async def evalluacmd(self, message):
        """Evaluate a Lua code"""
        prog = utils.get_args_raw(message)
        exec_cmd = f"{self.db.get('luaeval','compiler','lua5.3')} a.lua"
        with open("a.lua", "w") as src:
            src.write(prog)
        result = subprocess.getoutput(exec_cmd)
        os.system("rm a.lua")
        await message.edit(
            self.strings("result", message).format(
                prog=prog,
                compilation=result,
                ),
            parse_mode="Markdown")
    async def luasetccmd(self, message):
        """Sets path or executable for lua compiler. Ex: .luaset luajit"""
        self.db.set("luaeval","compiler",utils.get_args_raw(message))
        await message.edit(
            "**✅ Compiler executable set successful!**",
            parse_mode="Markdown"
        )