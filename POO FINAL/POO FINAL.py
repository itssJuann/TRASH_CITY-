from datetime import datetime

class SistemaGestionDebasurasyresiduos:
    def __init__(self):
        self.rutas = []

    def nuevaRuta(self, ruta):
        self.rutas.append(ruta)

    def quitarRuta(self, ruta):
        self.rutas.remove(ruta)

    def conseguirRutas(self):
        return self.rutas

    
    def obtenerVidrioRecogidoPorFecha(self, fecha):
        vidrio_total = 0.0
        for ruta in self.rutas:
            if ruta.Fecha().date() == fecha.date():
                vidrio_total += ruta.conseguirCamion().Turno().VidrioRecogido()
        return vidrio_total

class indicacionesDedireccion:
    def __init__(self):
        self.puntos = []
        self.camion = None
        self.fecha = None

    def ponerPunto(self, punto):
        self.puntos.append(punto)

    def quitarPunto(self, punto):
        self.puntos.remove(punto)

    def conseguirPuntos(self):
        return self.puntos

    def conseguirCamion(self):
        return self.camion
    
     
    def asignarFecha(self, fecha):
        self.fecha = fecha

    def Fecha(self):
        return self.fecha

    def asignarCamion(self, camion):
        self.camion = camion

class PuntoGeo:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud

    def Lat(self):
        return self.latitud

    def asignarLat(self, latitud):
        self.latitud = latitud

    def Long(self):
        return self.longitud

    def asignarLong(self, longitud):
        self.longitud = longitud

class Camion:
    def __init__(self, conductor, asistentes, turno):
        self.conductor = conductor
        self.asistentes = asistentes
        self.turno = turno

    def Conductor(self):
        return self.conductor

    def asignarConductor(self, conductor):
        self.conductor = conductor

    def conseguirAsistentes(self):
        return self.asistentes

    def Asistente(self, asistente):
        self.asistentes.append(asistente)

    def conseguirAsistente(self, asistente):
        self.asistentes.remove(asistente)

    def Turno(self):
        return self.turno

    def asignarTurno(self, turno):
        self.turno = turno

class Personal:
    def __init__(self, identificacion):
        self.identificacion = identificacion

    def ID(self):
        return self.identificacion

    def asignarID(self, identificacion):
        self.identificacion = identificacion

class Turno:
    def __init__(self, fecha, hora_inicio, hora_fin):
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.vidrio_recogido = 0.0

    def Fecha(self):
        return self.fecha

    def asignarFecha(self, fecha):
        self.fecha = fecha

    def HoraInicio(self):
        return self.hora_inicio

    def asignarHoraInicio(self, hora_inicio):
        self.hora_inicio = hora_inicio

    def HoraFin(self):
        return self.hora_fin

    def asignarHoraFin(self, hora_fin):
        self.hora_fin = hora_fin

    def VidrioRecogido(self):
        return self.vidrio_recogido

    def asignarVidrioRecogido(self, vidrio_recogido):
        self.vidrio_recogido = vidrio_recogido

        from datetime import datetime
import unittest

class TestSistemaGestionResiduos(unittest.TestCase):
    def setUp(self):
        self.sistema = SistemaGestionDebasurasyresiduos()

        # Crear puntos geográficos
        punto1 = PuntoGeo(10.0, 20.0)
        punto2 = PuntoGeo(15.0, 25.0)
        punto3 = PuntoGeo(12.0, 22.0)

        # Crear una persona
        conductor = Personal("1234567890")

        # Crear asistentes
        asistente1 = Personal("9876543210")
        asistente2 = Personal("5678901234")

        # Crear un turno
        fecha = datetime(2023, 5, 19)
        hora_inicio = datetime(2023, 5, 19, 8, 0)
        hora_fin = datetime(2023, 5, 19, 12, 0)
        turno = Turno(fecha, hora_inicio, hora_fin)

        # Crear una ruta
        ruta = indicacionesDedireccion()
        ruta.asignarFecha(fecha)  # Asignar la fecha a la instancia de indicacionesDedireccion
        ruta.ponerPunto(punto1)
        ruta.ponerPunto(punto2)
        ruta.ponerPunto(punto3)

        # Crear un camión
        camion = Camion(conductor, [asistente1, asistente2], turno)

        # Asignar camión a la ruta
        ruta.asignarCamion(camion)

        # Asignar ruta al sistema
        self.sistema.nuevaRuta(ruta)

    def testObtenerVidrioRecogidoPorFecha(self):
        fecha = datetime(2023, 5, 19)
        vidrio_total = self.sistema.obtenerVidrioRecogidoPorFecha(fecha)
        self.assertEqual(vidrio_total, 0.0)

        # Asignar vidrio recogido al turno
        turno = self.sistema.conseguirRutas()[0].conseguirCamion().Turno()
        turno.asignarVidrioRecogido(5.7)

        # Verificar que se obtenga la cantidad correcta de vidrio recogido
        vidrio_total = self.sistema.obtenerVidrioRecogidoPorFecha(fecha)
        self.assertEqual(vidrio_total, 5.7)

if __name__ == '__main__':
    unittest.main()