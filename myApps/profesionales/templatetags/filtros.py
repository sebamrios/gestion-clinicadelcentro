from django import template

register = template.Library()

@register.filter
def filtrar_especialidad(profesionales, especialidad_id):
    """
    Filtra la lista de profesionales según la especialidad.
    Si especialidad_id es None o 'todas', devuelve todos los profesionales.
    """
    if not especialidad_id or especialidad_id == "todas":
        return profesionales
    # Convertir especialidad_id a entero
    especialidad_id = int(especialidad_id)
    profesionales_filtrados = []
    for p in profesionales:
        if p.especialidad.id == especialidad_id:
            profesionales_filtrados.append(p)
    return profesionales_filtrados