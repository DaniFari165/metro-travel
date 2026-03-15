class Aeropuerto:
    def __init__(self, codigo, nombre, requiere_visa):
        self.codigo = codigo.strip().upper()
        self.nombre = nombre.strip()
        self.requiere_visa = requiere_visa

    def __str__(self):
        visa = "Sí" if self.requiere_visa else "No"
        return f"{self.codigo} - {self.nombre} (Requiere visa: {visa})"