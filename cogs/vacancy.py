import disnake
from disnake.ext import commands 

intents = disnake.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='s.', intents=intents) 
bot.remove_command("help")

class reject_modal(disnake.ui.Modal):
    def __init__(self, user, who, *args, **kwargs) -> None:
        self.user = user
        self.who = who
        
        components = [
            disnake.ui.TextInput(label="Причина", min_length=3, custom_id="reject")
        ]

        super().__init__(*args, **kwargs, components=components)

    async def callback(self, interaction: disnake.Interaction):
        embed = disnake.Embed(title="Статус вашей заявки изменен.", description=f"Статус вашей заявки на **{self.who}** изменен на `Отклонен`.\n > **Причина:** \n ```{interaction.text_values["reject"]}```")  
        await self.user.send(embed=embed)
        await interaction.response.send_message('Данные отправлены!', ephemeral = True)

        

class push_vacancy_moder(disnake.ui.View):
    def __init__(self, *, timeout = None, user: disnake.Member, msg: disnake.Message, name_qs, device_qs, exp_qs, mod_vs, time_qs) -> None:
        self.name_qs = name_qs
        self.devise_qs = device_qs
        self.exp_qs = exp_qs
        self.mod_vs = mod_vs
        self.time_qs = time_qs
        self.msg = msg
        self.user = user
        super().__init__(timeout=timeout)
    @disnake.ui.select(
    placeholder = 'Выберите действие',
    min_values = 1, 
    max_values = 1,
    options = [
    disnake.SelectOption(
            label='Одобрить', emoji="✅"),
        disnake.SelectOption(
            label='Отклонить', emoji="❌")
    ]
    )
    
    async def callback(self, select, interaction: disnake.AppCommandInteraction):
        if select.values[0] == 'Одобрить':
            embed = disnake.Embed(title='Заявка на Moderator')
            embed.add_field(name='Подающий:', value = f'{self.user.mention}')
            embed.add_field(name='Имя, возраст:', value = "```" + self.name_qs + "```", inline = False)
            embed.add_field(name='Опыт работы:', value = "```" + self.devise_qs + "```", inline = False)
            embed.add_field(name='Время в неделю:', value = "```" + self.exp_qs + "```", inline = False)
            embed.add_field(name='Идеи на счет сервера:', value = "```" + self.mod_vs + "```", inline = False)
            embed.add_field(name='Лучшие качества:', value = "```" + self.time_qs + "```", inline = False)
            
            embed.set_thumbnail(url=f'{self.user.avatar.url}')
            
            member = self.user
            massage_id = self.msg.id

            role = interaction.guild.get_role(1259738528934268945)
            embed = disnake.Embed(title="Статус вашей заявки изменен.", description=f"Статус вашей заявки на **Moderator** изменен на `Одобрено`.\n Скоро вам назначат собеседование")
            
            await member.add_roles(role)
            await member.send(embed=embed)

            await self.msg.edit(f"Статус: Одобрено. Изменил: {interaction.user.mention} \n `1.`<@&1259738528934268945> - роль успешно выдана", view=None)
        elif select.values[0] == 'Отклонить':
            embed = disnake.Embed(title='Заявка на Moderator')
            embed.add_field(name='Подающий:', value = f'{self.user.mention}')
            embed.add_field(name='Имя, возраст:', value = "```" + self.name_qs + "```", inline = False)
            embed.add_field(name='Опыт работы:', value = "```" + self.devise_qs + "```", inline = False)
            embed.add_field(name='Время в неделю:', value = "```" + self.exp_qs + "```", inline = False)
            embed.add_field(name='Идеи на счет сервера:', value = "```" + self.mod_vs + "```", inline = False)
            embed.add_field(name='Лучшие качества:', value = "```" + self.time_qs + "```", inline = False)
            
            embed.set_thumbnail(url=f'{self.user.avatar.url}')
            
            member = self.user

            reject = reject_modal(title="Причина", who="Moderator", user=member)
            await interaction.response.send_modal(reject)

            await self.msg.edit(f"Статус: Отклонен. Изменил: {interaction.user.mention}", view=None)

class push_vacancy_support(disnake.ui.View):
    def __init__(self, *, timeout = None, user: disnake.Member, msg: disnake.Message, name_qs, device_qs, exp_qs, event_qs, time_qs) -> None:
        self.name_qs = name_qs
        self.devise_qs = device_qs
        self.exp_qs = exp_qs
        self.event_qs = event_qs
        self.time_qs = time_qs
        self.msg = msg
        self.user = user
        super().__init__(timeout=timeout)
    @disnake.ui.select(
    placeholder = 'Выберите действие',
    min_values = 1, 
    max_values = 1,
    options = [
    disnake.SelectOption(
            label='Одобрить', emoji="✅"),
        disnake.SelectOption(
            label='Отклонить', emoji="❌")
    ]
    )
    
    async def callback(self, select, interaction: disnake.AppCommandInteraction):
        if select.values[0] == 'Одобрить':
            embed = disnake.Embed(title='Заявка на Support')
            embed.add_field(name='Подающий:', value = f'{self.user.mention}')
            embed.add_field(name='Имя, возраст:', value = "```" + self.name_qs + "```", inline = False)
            embed.add_field(name='Опыт работы:', value = "```" + self.devise_qs + "```", inline = False)
            embed.add_field(name='Время в неделю:', value = "```" + self.exp_qs + "```", inline = False)
            embed.add_field(name='Идеи на счет сервера:', value = "```" + self.event_qs + "```", inline = False)
            embed.add_field(name='Лучшие качества:', value = "```" + self.time_qs + "```", inline = False)
            embed.set_thumbnail(url=f'{self.user.avatar.url}')
            
            
            member = self.user

            role = interaction.guild.get_role(1260967414527561858)
            embed = disnake.Embed(title="Статус вашей заявки изменен.", description=f"Статус вашей заявки на **Support** изменен на `Одобрено`.\n Скоро вам назначат собеседование")
            
            await member.add_roles(role)
            await member.send(embed=embed)

            await self.msg.edit(f"Статус: Одобрено. Изменил: {interaction.user.mention} \n `1.`<@&1260967414527561858> - роль успешно выдана", view=None)
        elif select.values[0] == 'Отклонить':
            embed = disnake.Embed(title='Заявка на Support')
            embed.add_field(name='Подающий:', value = f'{self.user.mention}')
            embed.add_field(name='Имя, возраст:', value = "```" + self.name_qs + "```", inline = False)
            embed.add_field(name='Опыт работы:', value = "```" + self.devise_qs + "```", inline = False)
            embed.add_field(name='Время в неделю:', value = "```" + self.exp_qs + "```", inline = False)
            embed.add_field(name='Идеи на счет сервера:', value = "```" + self.event_qs + "```", inline = False)
            embed.add_field(name='Лучшие качества:', value = "```" + self.time_qs + "```", inline = False)
            embed.set_thumbnail(url=f'{self.user.avatar.url}')
            
            member = self.user

            reject = reject_modal(title="Причина", who="Support", user=member)
            await interaction.response.send_modal(reject)

            await self.msg.edit(f"Статус: Отклонен. Изменил: {interaction.user.mention}", view=None)

class push_vacancy_piar(disnake.ui.View):
    def __init__(self, *, timeout = None, user: disnake.Member, msg: disnake.Message, name_qs, device_qs, creative_qs, time_pos, online) -> None:
        self.name_qs = name_qs
        self.devise_qs = device_qs
        self.creative_qs = creative_qs
        self.time_pos = time_pos
        self.msg = msg
        self.user = user
        self.online = online
        super().__init__(timeout=timeout)
    @disnake.ui.select(
    placeholder = 'Выберите действие',
    min_values = 1, 
    max_values = 1,
    options = [
    disnake.SelectOption(
            label='Одобрить', emoji="✅"),
        disnake.SelectOption(
            label='Отклонить', emoji="❌")
    ]
    )
    
    async def callback(self, select, interaction: disnake.AppCommandInteraction):
        if select.values[0] == 'Одобрить':
            embed = disnake.Embed(title='Заявка на Пиар-Менеджер')
            embed.add_field(name='Подающий:', value = f'{self.user.mention}')
            embed.add_field(name='Имя, возраст:', value = "```" + self.name_qs + "```", inline = False)
            embed.add_field(name='Опыт работы:', value = "```" + self.devise_qs + "```", inline = False)
            embed.add_field(name='Время в неделю:', value = "```" + self.creative_qs + "```", inline = False)
            embed.add_field(name='Идеи на счет сервера:', value = "```" + self.time_pos + "```", inline = False)
            embed.add_field(name='Лучшие качества:', value = "```" + self.online + "```", inline = False)
            embed.set_thumbnail(url=f'{self.user.avatar.url}')
            
            
            member = self.user

            role = interaction.guild.get_role(1259738528934268944)
            embed = disnake.Embed(title="Статус вашей заявки изменен.", description=f"Статус вашей заявки на **Пиар-Менеджер** изменен на `Одобрено`.\n Скоро вам назначат собеседование")
            
            await member.add_roles(role)
            await member.send(embed=embed)

            await self.msg.edit(f"Статус: Одобрено. Изменил: {interaction.user.mention} \n `1.`<@&1259738528934268944> - роль успешно выдана", view=None)
        elif select.values[0] == 'Отклонить':
            embed = disnake.Embed(title='Заявка на Пиар-Менеджер')
            embed.add_field(name='Подающий:', value = f'{self.user.mention}')
            embed.add_field(name='Имя, возраст:', value = "```" + self.name_qs + "```", inline = False)
            embed.add_field(name='Опыт работы:', value = "```" + self.devise_qs + "```", inline = False)
            embed.add_field(name='Время в неделю:', value = "```" + self.creative_qs + "```", inline = False)
            embed.add_field(name='Идеи на счет сервера:', value = "```" + self.time_pos + "```", inline = False)
            embed.add_field(name='Лучшие качества:', value = "```" + self.online + "```", inline = False)
            embed.set_thumbnail(url=f'{self.user.avatar.url}')
            
            member = self.user

            reject = reject_modal(title="Причина", who="Пиар-Менеджер", user=member)
            await interaction.response.send_modal(reject)

            await self.msg.edit(f"Статус: Отклонен. Изменил: {interaction.user.mention}", view=None)
            
class push_vacancy_eventMod(disnake.ui.View):
    def __init__(self, *, timeout = None, user: disnake.Member, msg: disnake.Message, name_qs, exp_qs, time_pos, idea_qs, best_qs) -> None:
        self.name_qs = name_qs
        self.exp_qs = exp_qs
        self.time_pos = time_pos
        self.msg = msg
        self.user = user
        self.idea_qs = idea_qs
        self.best = best_qs
        super().__init__(timeout=timeout)
    @disnake.ui.select(
    placeholder = 'Выберите действие',
    min_values = 1, 
    max_values = 1,
    options = [
    disnake.SelectOption(
            label='Одобрить', emoji="✅"),
        disnake.SelectOption(
            label='Отклонить', emoji="❌")
    ]
    )
    
    async def callback(self, select, interaction: disnake.AppCommandInteraction):
        if select.values[0] == 'Одобрить':
            embed = disnake.Embed(title='Заявка на EventMod')
            embed.add_field(name='Подающий:', value = f'{self.user.mention}')
            embed.add_field(name='Имя, возраст:', value = "```" + self.name_qs + "```", inline = False)
            embed.add_field(name='Опыт работы:', value = "```" + self.exp_qs + "```", inline = False)
            embed.add_field(name='Время в неделю:', value = "```" + self.time_pos + "```", inline = False)
            embed.add_field(name='Идеи на счет сервера:', value = "```" + self.idea_qs + "```", inline = False)
            embed.add_field(name='Лучшие качества:', value = "```" + self.best + "```", inline = False)
            embed.set_thumbnail(url=f'{self.user.avatar.url}')
            
            
            member = self.user

            role = interaction.guild.get_role(1259738528934268943)
            embed = disnake.Embed(title="Ста`тус вашей заявки изменен.", description=f"Статус вашей заявки на **EventMod** изменен на `Одобрено`.\n Скоро вам назначат собеседование")
            
            await member.add_roles(role)
            await member.send(embed=embed)

            await self.msg.edit(f"Статус: Одобрено. Изменил: {interaction.user.mention} \n `1.`<@&1259738528934268943> - роль успешно выдана", view=None)
        elif select.values[0] == 'Отклонить':
            embed = disnake.Embed(title='Заявка на EventMod')
            embed.add_field(name='Подающий:', value = f'{self.user.mention}')
            embed.add_field(name='Имя, возраст:', value = "```" + self.name_qs + "```", inline = False)
            embed.add_field(name='Опыт работы:', value = "```" + self.exp_qs + "```", inline = False)
            embed.add_field(name='Время в неделю:', value = "```" + self.time_pos + "```", inline = False)
            embed.add_field(name='Идеи на счет сервера:', value = "```" + self.idea_qs + "```", inline = False)
            embed.add_field(name='Лучшие качества:', value = "```" + self.best + "```", inline = False)
            embed.set_thumbnail(url=f'{self.user.avatar.url}')
            
            member = self.user

            reject = reject_modal(title="Причина", who="EventMod", user=member)
            await interaction.response.send_modal(reject)

            await self.msg.edit(f"Статус: Отклонен. Изменил: {interaction.user.mention}", view=None)

class moder (disnake.ui.Modal):
    def __init__(self, bot, *args, **kwargs) -> None:
        self.bot: commands.Bot = bot

        components = [
            disnake.ui.TextInput(label="Имя и возраст (14+)", placeholder='Алексей, 18', min_length=5, custom_id="name"),
            disnake.ui.TextInput(label="Опыт работы", placeholder='Я был...', min_length=2, custom_id="device"),
            disnake.ui.TextInput(label="Время в неделю", placeholder='5+ часов', min_length=2, custom_id="exp"),
            disnake.ui.TextInput(label="Ваши идеи на счет сервера", placeholder='сделай НСФВ канал', min_length=2, custom_id="mod_voice"),
            disnake.ui.TextInput(label="Укажите ваши лучшие качества", placeholder='активный, инициативный, могу влиять на людей', min_length=3, custom_id="time")
        ]

        super().__init__(*args, **kwargs, components=components)

    async def callback(self, interaction: disnake.ModalInteraction):

        embed = disnake.Embed(title='Заявка на Moderator')
        embed.add_field(name='Подающий:', value = f'{interaction.user.mention}')
        embed.add_field(name='Имя, возраст:', value = "```" + interaction.text_values.get("name") + "```", inline = False)
        embed.add_field(name='Опыт работы:', value = "```" + interaction.text_values.get("device") + "```", inline = False)
        embed.add_field(name='Время в неделю:', value = "```" + interaction.text_values.get("exp") + "```", inline = False)
        embed.add_field(name='Идеи на счет сервера:', value = "```" + interaction.text_values.get("mod_voice") + "```", inline = False)
        embed.add_field(name='Лучшие качества:', value = "```" + interaction.text_values.get("time") + "```", inline = False)
        

        embed.set_thumbnail(url=f'{interaction.user.avatar.url}')
        channel_id = 1267198328446259325
        channel = interaction.bot.get_channel(channel_id)
        msg = await channel.send(embed=embed)
        await msg.edit(embed=embed, view=push_vacancy_moder(user=interaction.user, name_qs=interaction.text_values["name"], device_qs=interaction.text_values["device"], exp_qs=interaction.text_values["exp"], mod_vs=interaction.text_values["mod_voice"], time_qs=interaction.text_values["time"], msg=msg))
        
        embed_wait = disnake.Embed()
        embed_wait.add_field(name="Ваша заявка на рассмотрении", value="Ожидайте ответ...", inline=True)
        embed_wait.set_thumbnail(url=f"{interaction.user.avatar.url}")
        await interaction.response.send_message(embed=embed_wait, ephemeral = True)


class support(disnake.ui.Modal):
    def __init__(self, bot, *args, **kwargs) -> None:
        self.bot = bot

        components = [
            disnake.ui.TextInput(label="Имя и возраст (14+)", placeholder='Алексей, 18', min_length=5, custom_id="name"),
            disnake.ui.TextInput(label="Опыт работы", placeholder='Я был...', min_length=2, custom_id="device"),
            disnake.ui.TextInput(label="Время в неделю", placeholder='5+ часов', min_length=2, custom_id="exp"),
            disnake.ui.TextInput(label="Идеи на счет сервера", placeholder='сделай НСФВ канал', min_length=2, custom_id="mod_voice"),
            disnake.ui.TextInput(label="Укажите ваши лучшие качества", placeholder='активный, инициативный, могу влиять на людей', min_length=3, custom_id="time")
        ]

        super().__init__(*args, **kwargs, components=components)

    async def callback(self, interaction: disnake.Interaction):
        embed = disnake.Embed(title='Заявка на Support')
        embed.add_field(name='Подающий:', value = f'{interaction.user.mention}')
        embed.add_field(name='Имя, возраст:', value = "```" + interaction.text_values.get("name") + "```", inline = False)
        embed.add_field(name='Опыт работы:', value = "```" + interaction.text_values.get("device") + "```", inline = False)
        embed.add_field(name='Время в неделю:', value = "```" + interaction.text_values.get("exp") + "```", inline = False)
        embed.add_field(name='Идеи на счет сервера:', value = "```" + interaction.text_values.get("mod_voice") + "```", inline = False)
        embed.add_field(name='Лучшие качества:', value = "```" + interaction.text_values.get("time") + "```", inline = False)
        embed.set_thumbnail(url=f'{interaction.user.avatar.url}')
        
        channel_id = 1267198328446259325
        channel = interaction.bot.get_channel(channel_id)
        msg = await channel.send(embed=embed)
        
        await msg.edit(embed=embed, view=push_vacancy_support(user=interaction.user, name_qs=interaction.text_values["name"], device_qs=interaction.text_values["device"], exp_qs=interaction.text_values["exp"], event_qs=interaction.text_values["mod_voice"], time_qs=interaction.text_values["time"], msg=msg))
        
        embed_wait = disnake.Embed()
        embed_wait.add_field(name="Ваша заявка на рассмотрении", value="Ожидайте ответ...", inline=True)
        embed_wait.set_thumbnail(url=f"{interaction.user.avatar.url}")
        await interaction.response.send_message(embed=embed_wait, ephemeral = True)

class piar(disnake.ui.Modal):
    def __init__(self, bot, *args, **kwargs) -> None:
        self.bot = bot

        components = [
            disnake.ui.TextInput(label="Имя и возраст (14+)", placeholder='Алексей, 18', min_length=5, custom_id="name"),
            disnake.ui.TextInput(label="Опыт работы", placeholder='Я был...', min_length=2, custom_id="device"),
            disnake.ui.TextInput(label="Время в неделю", placeholder='5+ часов', min_length=2, custom_id="exp"),
            disnake.ui.TextInput(label="Идеи на счет сервера", placeholder='сделай НСФВ канал', min_length=2, custom_id="mod_voice"),
            disnake.ui.TextInput(label="Укажите ваши лучшие качества", placeholder='активный, инициативный, могу влиять на людей', min_length=3, custom_id="time")
        ]
        
        super().__init__(*args, **kwargs, components=components)

    async def callback(self, interaction: disnake.Interaction):
        embed = disnake.Embed(title='Заявка на Пиар-Менеджера')
        embed.add_field(name='Подающий', value = f'{interaction.user.mention}')
        embed.add_field(name='Имя, возраст', value = "```" + interaction.text_values.get("name") + "```", inline = False)
        embed.add_field(name='Опыт работы', value = "```" + interaction.text_values.get("device") + "```", inline = False)
        embed.add_field(name='Время в неделю', value = "```" + interaction.text_values.get("exp") + "```", inline = False)
        embed.add_field(name='Идеи на счет сервера', value = "```" + interaction.text_values.get("mod_voice") + "```", inline = False)
        embed.add_field(name='Лучшие качества', value = "```" + interaction.text_values.get("time") + "```", inline = False)
        embed.set_thumbnail(url=f'{interaction.user.avatar.url}')

        channel_id = 1267198328446259325
        channel = interaction.bot.get_channel(channel_id)
        msg = await channel.send(embed=embed)
        
        await msg.edit(embed=embed, view=push_vacancy_piar(user=interaction.user, name_qs=interaction.text_values["name"], device_qs=interaction.text_values["device"], time_pos=interaction.text_values["mod_voice"], creative_qs=interaction.text_values["time"], online=interaction.text_values["time"], msg=msg))

        embed_wait = disnake.Embed()
        embed_wait.add_field(name="Ваша заявка на рассмотрении", value="Ожидайте ответ...", inline=True)
        embed_wait.set_thumbnail(url=f"{interaction.user.avatar.url}")
        await interaction.response.send_message(embed=embed_wait, ephemeral = True)

class eventMod(disnake.ui.Modal):
    def __init__(self, bot, *args, **kwargs) -> None:
        self.bot = bot

        components = [
            disnake.ui.TextInput(label="Имя и возраст (14+)", placeholder='Алексей, 18', min_length=5, custom_id="name"),
            disnake.ui.TextInput(label="Опыт работы", placeholder='Я был...', min_length=2, custom_id="exp"),
            disnake.ui.TextInput(label="Время в неделю", placeholder='5+ часов', min_length=2, custom_id="time"),
            disnake.ui.TextInput(label="Идеи на счет сервера", placeholder='сделай НСФВ канал', min_length=2, custom_id="idea"),
            disnake.ui.TextInput(label="Укажите ваши лучшие качества", placeholder='активный, инициативный, могу влиять на людей', min_length=3, custom_id="best")
        ]

        super().__init__(*args, **kwargs, components=components)

    async def callback(self, interaction: disnake.Interaction):
        embed = disnake.Embed(title='Заявка на EventMod')
        embed.add_field(name='Подающий', value=f'{interaction.user.mention}')
        embed.add_field(name='Имя, возраст', value="```" + interaction.text_values.get("name") + "```", inline=False)
        embed.add_field(name='Опыт работы', value = "```" + interaction.text_values.get("exp") + "```", inline = False)
        embed.add_field(name='Время в неделю', value="```" + interaction.text_values.get("time") + "```", inline=False)
        embed.add_field(name='Идеи на счет сервера', value="```" + interaction.text_values.get("idea") + "```", inline=False)
        embed.add_field(name='Лучшие качества', value="```" + interaction.text_values.get("best") + "```", inline=False)
        embed.set_thumbnail(url=f'{interaction.user.avatar.url}')

        channel_id = 1267198328446259325
        channel = interaction.bot.get_channel(channel_id)
        msg = await channel.send(embed=embed)

        await msg.edit(embed=embed, view=push_vacancy_eventMod(user=interaction.user, name_qs=interaction.text_values["name"], exp_qs=interaction.text_values["exp"], time_pos=interaction.text_values["time"], idea_qs=interaction.text_values["idea"], best_qs=interaction.text_values["best"], msg=msg))

        embed_wait = disnake.Embed()
        embed_wait.add_field(name="Ваша заявка на рассмотрении", value="Ожидайте ответ...", inline=True)
        embed_wait.set_thumbnail(url=f"{interaction.user.avatar.url}")
        await interaction.response.send_message(embed=embed_wait, ephemeral = True)

class MyView(disnake.ui.View):
    @disnake.ui.select( 
        placeholder = 'Выберите заявку для подачи', 
        min_values = 1, 
        max_values = 1, 
        options = [ 
            disnake.SelectOption(
                label="Moderator",
                description="Полная модерация сервера."),
            disnake.SelectOption(
                label="Support",
                description="Помощь новичкам и их адаптация по серверу."),
            disnake.SelectOption(
                label="Пиар-Менеджер",
                description="Привлечения новых участников."),
            disnake.SelectOption(
                label="EventMod",
                description="Проведения мероприятий." )
        ]
    )

    async def select_callback(self, select, interaction):
        if select.values[0] == 'Moderator':
            moder_modal = moder(bot,title='Заявка на Moderator')
            await interaction.response.send_modal(moder_modal)
        elif select.values[0] == 'Support':
            support_modal = support(bot,title='Заявка на Support')
            await interaction.response.send_modal(support_modal)
        elif select.values[0] == 'Пиар-Менеджер':
            piar_modal = piar(bot, title='Заявка на Пиар-Менеджерa')
            await interaction.response.send_modal(piar_modal)
        elif select.values[0] == 'EventMod':
            eventMod_modal = eventMod(bot,title='Заявка на EventMod')
            await interaction.response.send_modal(eventMod_modal)

class Vacancy(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.command()
    #@commands.has_permissions(administrator = True)
    async def vacancy(self, ctx: commands.Context):
        embed = disnake.Embed()
        embed.set_image(url='https://media.discordapp.net/attachments/1262270134504919122/1265945169505681491/magicly-1714056933153.png?ex=66a74f50&is=66a5fdd0&hm=ac3f5604ad6683798ab7e7be40f0500daf951ff8fe8d465b08a7fffeba0d7f29&=&format=webp&quality=lossless&width=550&height=172')
        embed1 = disnake.Embed(title='Заявки',
            description='Давно хотел быть частью сервера?\nПроводить ивенты, следить за чатом, и т.п?\n\nТогда ждём тебя в нашем дружном коллективе!\n\nНа данный момент мы ищем: PR-менеджера, Модератора, Ивентера, Саппорта.\nМы оставляем за собой право отказать вам в заявке, если вы не подходите по каким-либо критериям.\n\nЗа шуточные заявки вы можете получить наказание.')
        
        guild = bot.get_guild(1259738528871354368)

        await ctx.bot.get_channel(1260965070494503005).send(embed = embed)
        await ctx.bot.get_channel(1260965070494503005).send(embed = embed1, view=MyView())
        await ctx.bot.reply('Набор отправлен!')

    @commands.Cog.listener()
    async def on_ready(self):
        #await self.bot.wait_until_ready()  # Убедитесь, что бот полностью загрузился

        embed = disnake.Embed()
        embed.set_image(url='https://media.discordapp.net/attachments/1262270134504919122/1265945169505681491/magicly-1714056933153.png?ex=66a74f50&is=66a5fdd0&hm=ac3f5604ad6683798ab7e7be40f0500daf951ff8fe8d465b08a7fffeba0d7f29&=&format=webp&quality=lossless&width=550&height=172')
        embed1 = disnake.Embed(
            title='О наборе',
            description='Давно хотел быть частью сервера?\nПроводить ивенты, следить за чатом, и т.п?\n\nТогда ждём тебя в нашем дружном коллективе!\n\nНа данный момент мы ищем: PR-менеджера, Модератора, Ивентера, Саппорта.\nМы оставляем за собой право отказать вам в заявке, если вы не подходите по каким-либо критериям.\n\nЗа шуточные заявки вы можете получить наказание.\n\n ・Moderator — Полная модерация сервера \n ・Support — Помощь новичкам и их адаптация по серверу. \n ・Пиар-Менеджер — Привлечения новых участников. \n ・EventMod — Проведения мероприятий.'
        )

        channel_id = 1260965070494503005
        channel = self.bot.get_channel(channel_id)
        
        if channel:
            # Очистить последние 5 сообщений (если требуется)
            await channel.purge(limit=5)

            await channel.send(embed=embed)
            await channel.send(embed=embed1, view=MyView())
        else:
            print("LOG: канал не найден.")

def setup(bot: commands.Bot):
    bot.add_cog(Vacancy(bot))