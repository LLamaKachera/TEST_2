fun main() {
    println("Ingrese su año de nacimiento:")
    val anoNacimiento = readLine()!!.toInt()
    println("Ingrese el año actual:")
    val anoActual = readLine()!!.toInt()
    
    val anosVividos = anoActual - anoNacimiento
    val diasVividos = anosVividos * 365
    
    println("Días vividos: $diasVividos")
}
