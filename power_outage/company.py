__all__ = ['company']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['data'])
var.put('data', Js({'fuente':Js('Web Service'),'empresa':Js('EDENOR'),'totalUsuariosSinSuministro':Js('274'),'totalUsuariosConSuministro':Js('2.998.217'),'ultimaActualizacion':Js('16:25'),'totalUsuariosAyer':Js('32.933'),'cortesPreventivos':Js([]),'cortesProgramados':Js([Js({'partido':Js('GRAL LAS HERAS'),'localidad':Js('GRAL LAS HERAS'),'subestacion_alimentador':Js('363-MARCOS PAZ / R:363-TR3 / 363-5472 / 132-5523'),'usuarios':Js('3'),'normalizacion':Js('2020-04-08 16:57')}), Js({'partido':Js('MORENO'),'localidad':Js('FRANCISCO ALVAREZ'),'subestacion_alimentador':Js('263- / R:263-TR2 / 263-5521'),'usuarios':Js('256'),'normalizacion':Js('2020-04-08 20:00')})]),'cortesServicioMedia':Js([]),'cortesComunicados':Js([]),'cortesServicioBaja':Js([Js({'partido':Js('MORENO'),'localidad':Js('TRUJUI'),'usuarios':Js('15')})])}))


# Add lib to the module scope
company = var.to_python()