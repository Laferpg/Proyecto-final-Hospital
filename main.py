from controllers.persona_controller import PersonaController
from controllers.especialidad_controller import EspecialidadController
from controllers.ingreso_controller import IngresoController
from controllers.zona_controller import ZonaController
from controllers.cama_controller import CamaController
from controllers.habitacion_controller import HabitacionController

from menu.menu_principal import menu_principal



def main():
    
    persona_controller = PersonaController()
    especialidad_controller = EspecialidadController()
    ingreso_controller = IngresoController()
    zona_controller = ZonaController()
    cama_controller = CamaController()
    habitacion_controller = HabitacionController()

    menu_principal(
        persona_controller,
        especialidad_controller,
        ingreso_controller,
        zona_controller,
        cama_controller,
        habitacion_controller
    )
    

if __name__ == "__main__":
    main()