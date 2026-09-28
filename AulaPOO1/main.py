class Reserva:

    lista_reservas = []

    def __init__(self, nome_responsavel, data, hora, quantidade_pessoas):
        self.nome_responsavel = nome_responsavel
        self.data = data
        self.hora = hora
        self.quantidade_pessoas = quantidade_pessoas
        Reserva.lista_reservas.append(self)


    def reservarMesa(nome_responsavel, data, hora, quantidade_pessoas):
        reserva = Reserva(nome_responsavel, data, hora, quantidade_pessoas)

        return f'Reserva realizada com sucesso para {reserva.nome_responsavel} no dia {reserva.data} às {reserva.hora} para {reserva.quantidade_pessoas} pessoas.'
    
    def consultarReserva(nome_responsavel, data, hora):
        for reserva in Reserva.lista_reservas:
            if reserva.nome_responsavel == nome_responsavel and reserva.data == data and reserva.hora == hora:
             return f'Reserva encontrada: {reserva.nome_responsavel} no dia {reserva.data} às {reserva.hora} para {reserva.quantidade_pessoas} pessoas.'
        return f'Reserva não encontrada para {nome_responsavel} no dia {data} às {hora}.'

    @Property
    def listaReservas(self):
        return self.lista_reservas

reserva1 = reservarMesa("João", "2023-07-15", "19:00", 4)
print(consultarReserva("João", "2023-07-15", "19:00"))
print(listaReservas)