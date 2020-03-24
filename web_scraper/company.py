__all__ = ['company']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['data'])
var.put('data', Js({'fuente':Js('Web Service'),'empresa':Js('EDENOR'),'totalUsuariosSinSuministro':Js('3.364'),'totalUsuariosConSuministro':Js('2.995.127'),'ultimaActualizacion':Js('9:55'),'totalUsuariosAyer':Js('18.504'),'cortesPreventivos':Js([]),'cortesProgramados':Js([]),'cortesServicioMedia':Js([Js({'partido':Js(''),'localidad':Js(''),'subestacion_alimentador':Js('263- / R:263-TR2 / 263-5525'),'usuarios':Js('144'),'normalizacion':Js('2020-03-24 14:00')}), Js({'partido':Js('MORENO'),'localidad':Js('CUARTEL V'),'subestacion_alimentador':Js('263- / R:263-TR2 / 263-5525'),'usuarios':Js('2978'),'normalizacion':Js('2020-03-24 14:00')}), Js({'partido':Js('MORENO'),'localidad':Js('MORENO'),'subestacion_alimentador':Js('263- / R:263-TR2 / 263-5525'),'usuarios':Js('186'),'normalizacion':Js('2020-03-24 14:00')})]),'cortesComunicados':Js([]),'cortesServicioBaja':Js([Js({'partido':Js('CAPITAL FEDERAL'),'localidad':Js('BELGRANO'),'usuarios':Js('13')}), Js({'partido':Js('MALVINAS ARGENTINAS'),'localidad':Js('GRAND BOURG'),'usuarios':Js('21')}), Js({'partido':Js('MERLO'),'localidad':Js('LIBERTAD'),'usuarios':Js('11')}), Js({'partido':Js('MORENO'),'localidad':Js('MORENO'),'usuarios':Js('6')}), Js({'partido':Js('PILAR'),'localidad':Js('VILLA ROSA'),'usuarios':Js('5')})])}))


# Add lib to the module scope
company = var.to_python()