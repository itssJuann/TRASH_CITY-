from datetime import datetime

class SistemaGestionResiduos:
    def __init__(self):
        self.rutas = []

    def agregarRuta(self, ruta):
        self.rutas.append(ruta)

    def eliminarRuta(self, ruta):
        self.rutas.remove(ruta)

    def obtenerRutas(self):
        return self.rutas

    def obtenerVidrioRecogidoPorFecha(self, fecha):
        vidrio_total = 0.0
        for ruta in self.rutas:
            if ruta.obtenerCamion().obtenerTurno().obtenerFecha().date() == fecha.date():
                vidrio_total += ruta.obtenerCamion().obtenerTurno().obtenerVidrioRecogido()
        return vidrio_total

class Ruta:
    def __init__(self):
        self.puntos = []
        self.camion = None

    def agregarPunto(self, punto):
        self.puntos.append(punto)

    def eliminarPunto(self, punto):
        self.puntos.remove(punto)

    def obtenerPuntos(self):
        return self.puntos

    def obtenerCamion(self):
        return self.camion

    def asignarCamion(self, camion):
        self.camion = camion

class PuntoGeografico:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud

    def obtenerLatitud(self):
        return self.latitud

    def asignarLatitud(self, latitud):
        self.latitud = latitud

    def obtenerLongitud(self):
        return self.longitud

    def asignarLongitud(self, longitud):
        self.longitud = longitud

class Camion:
    def __init__(self, conductor, asistentes, turno):
        self.conductor = conductor
        self.asistentes = asistentes
        self.turno = turno

    def obtenerConductor(self):
        return self.conductor

    def asignarConductor(self, conductor):
        self.conductor = conductor

    def obtenerAsistentes(self):
        return self.asistentes

    def agregarAsistente(self, asistente):
        self.asistentes.append(asistente)

    def eliminarAsistente(self, asistente):
        self.asistentes.remove(asistente)

    def obtenerTurno(self):
        return self.turno

    def asignarTurno(self, turno):
        self.turno = turno

class Persona:
    def __init__(self, identificacion):
        self.identificacion = identificacion

    def obtenerIdentificacion(self):
        return self.identificacion

    def asignarIdentificacion(self, identificacion):
        self.identificacion = identificacion

class Turno:
    def __init__(self, fecha, hora_inicio, hora_fin):
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.vidrio_recogido = 0.0

    def obtenerFecha(self):
        return self.fecha

    def asignarFecha(self, fecha):
        self.fecha = fecha

    def obtenerHoraInicio(self):
        return self.hora_inicio

    def asignarHoraInicio(self, hora_inicio):
        self.hora_inicio = hora_inicio

    def obtenerHoraFin(self):
        return self.hora_fin

    def asignarHoraFin(self, hora_fin):
        self.hora_fin = hora_fin

    def obtenerVidrioRecogido(self):
        return self.vidrio_recogido

    def asignarVidrioRecogido(self, vidrio_recogido):
        self.vidrio_recogido = vidrio_recogido

        from datetime import datetime
import unittest

class TestSistemaGestionResiduos(unittest.TestCase):
    def setUp(self):
        self.sistema = SistemaGestionResiduos()

        # Crear puntos geográficos
        punto1 = PuntoGeografico(10.0, 20.0)
        punto2 = PuntoGeografico(15.0, 25.0)
        punto3 = PuntoGeografico(12.0, 22.0)

        # Crear una ruta
        ruta = Ruta()
        ruta.agregarPunto(punto1)
        ruta.agregarPunto(punto2)
        ruta.agregarPunto(punto3)

        # Crear una persona
        conductor = Persona("1234567890")

        # Crear asistentes
        asistente1 = Persona("9876543210")
        asistente2 = Persona("5678901234")

        # Crear un turno
        fecha = datetime(2023, 5, 19)
        hora_inicio = datetime(2023, 5, 19, 8, 0)
        hora_fin = datetime(2023, 5, 19, 12, 0)
        turno = Turno(fecha, hora_inicio, hora_fin)

        # Crear un camión
        camion = Camion(conductor, [asistente1, asistente2], turno)

        # Asignar camión a la ruta
        ruta.asignarCamion(camion)

        # Asignar ruta al sistema
        self.sistema.agregarRuta(ruta)

    def testObtenerVidrioRecogidoPorFecha(self):
        fecha = datetime(2023, 5, 19)
        vidrio_total = self.sistema.obtenerVidrioRecogidoPorFecha(fecha)
        self.assertEqual(vidrio_total, 0.0)

        # Asignar vidrio recogido al turno
        turno = self.sistema.obtenerRutas()[0].obtenerCamion().obtenerTurno()
        turno.asignarVidrioRecogido(5.7)

        # Verificar que se obtenga la cantidad correcta de vidrio recogido
        vidrio_total = self.sistema.obtenerVidrioRecogidoPorFecha(fecha)
        self.assertEqual(vidrio_total, 5.7)

if __name__ == '__main__':
    unittest.main()
