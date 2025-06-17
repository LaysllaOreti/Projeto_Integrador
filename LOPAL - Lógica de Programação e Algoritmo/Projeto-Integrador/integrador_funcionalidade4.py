arquivo_csv = r'LOPAL_Integrador.csv'

df = pd.read_csv(arquivo_csv)

df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d', errors='coerce')

data_escolhida = datetime.strptime('16/11/2024', '%d/%m/%Y').date()

df_data = df[df['Date'].dt.date == data_escolhida]

if df_data.empty:
    print("Nenhum dado encontrado para a data 16/11/2024.")
else:

    linha = df_data.iloc[-1]
    mapa_niveis = {
        1: '🔴',
        2: '🟡',
        3: '🟢'
    }

    msg = f"Estoque em 16/11: "
    msg += f"Esteira 1: {mapa_niveis.get(linha['esteira1'])} | "
    msg += f"Esteira 2: {mapa_niveis.get(linha['esteira2'])} | "
    msg += f"Esteira 3: {mapa_niveis.get(linha['esteira3'])}"

    numero = '+5519995594323'

    agora = datetime.now() + timedelta(minutes=1)
    hora = agora.hour
    minuto = agora.minute

    print("Mensagem agendada para envio:")
    print(msg)

    kit.sendwhatmsg(numero, msg, hora, minuto)
