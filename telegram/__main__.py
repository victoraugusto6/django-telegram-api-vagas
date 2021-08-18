import requests
from dateutil.parser import parse
import telegram
from decouple import config
from telegram.ext import CommandHandler, Updater

TELEGRAM_TOKEN = config('TELEGRAM_TOKEN')
DEBUG = config('DEBUG')
APP_NAME_HEROKU = config('APP_NAME_HEROKU')


def data_parser(vaga):
    return f'{parse(vaga["disponivel_ate"]).day}/' \
           f'{parse(vaga["disponivel_ate"]).month}/{parse(vaga["disponivel_ate"]).year}\n' \
           f'{parse(vaga["disponivel_ate"]).hour}h{parse(vaga["disponivel_ate"]).minute}m'


def enviar_mensagem(message, update, context):
    return context.bot.send_message(
        chat_id=update.effective_chat.id, text=message, disable_web_page_preview=True,
        parse_mode=telegram.ParseMode.HTML)


def enviar_vagas(update, context):
    message = f'Olá, {update.message.from_user.first_name}! 😎\n'
    message += '<strong>Segue a lista de vagas:</strong>\n\n'

    enviar_mensagem(message, update, context)

    response = requests.get('https://django-telegram-api-vagas-2.herokuapp.com/vaga/')
    data = response.json()

    for vaga in data["vagas"]:
        if vaga["disponivel"] is True:
            vaga_formatada = '<strong>Vaga: </strong>' + '\n' + str(vaga["nome"]) + '\n\n'
            vaga_formatada += '<strong>Empresa: </strong>' + '\n' + str(vaga["empresa"]) + '\n\n'
            vaga_formatada += '<strong>Descrição: </strong>' + '\n' + str(vaga["descricao"]) + '\n\n'
            vaga_formatada += '<strong>Salário: </strong>' + '\n' + 'R$ ' + str(vaga["salario"]) + '\n\n'
            vaga_formatada += '<strong>Área: </strong>' + '\n' + str(vaga["area"]) + '\n\n'
            vaga_formatada += '<strong>Linguagem: </strong>' + '\n' + str(vaga["linguagem"]) + '\n\n'
            vaga_formatada += '<strong>Framework: </strong>' + '\n' + str(vaga["framework"]) + '\n\n'
            vaga_formatada += '<strong>Disponível: </strong>' + '\n' + 'Sim' + '\n\n'
            vaga_formatada += '<strong>Disponível até</strong>: ' + '\n' + str(data_parser(vaga)) + '\n\n'
            vaga_formatada += '<strong>Contato</strong>: ' + '\n' + str(vaga["contato"]) + '\n\n'

            enviar_mensagem(vaga_formatada, update, context)


def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("enviar_vagas", enviar_vagas))

    if DEBUG:
        updater.start_polling()

        updater.idle()
    else:
        port = config('PORT', cast=int)

        updater.start_webhook(listen="0.0.0.0",
                              port=port,
                              url_path=TELEGRAM_TOKEN)
        updater.bot.setWebhook(f'https://{APP_NAME_HEROKU}.herokuapp.com/{TELEGRAM_TOKEN}')

        updater.idle()


if __name__ == "__main__":
    print("Bot em execução.")
    main()
