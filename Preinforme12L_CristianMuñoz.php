<?php

$Presion_semanal=[110.06,107.89,108.45,108.49,109.03,110.11,109.87,119.38,
	119.35,116.34,117.73,120.01,118.19,119.53,117.09,118.03,
	118.65,117.47,117.49,109.65,110.44,110.51,107.38,109.26,
	106.18,109.36,106.61,105.16,110.11,105.48,108.37,107.59,
	108.91,108.35,109.57,122.56,124.44,125.97,121.03,121.22,
	122.41,122.15,124.52,123.35,125.76,121.08,122.29,105.42,
	110.67,107.73,105.76,107.85];

//Punto 1

$long=count($Presion_semanal);
$mayor=$Presion_semanal[0];
$menor=$Presion_semanal[0];
for ($i=0;$i<$long;$i++) {
	if ($mayor<$Presion_semanal[$i]) {
		$mayor=$Presion_semanal[$i];
	}
	elseif ($menor>$Presion_semanal[$i]){
		$menor=$Presion_semanal[$i];
	}	
}
$diferencia=round($mayor-$menor,2);
print "La diferencia entre la mayor y la menor presión promedio semanal es ".$diferencia."KPa"."<br>";
	
//Punto 2

$suma=0;
for ($i=0;$i<$long;$i++) {
	$suma+=$Presion_semanal[$i];
}
$media_presion=round($suma/$long,2);
print "La media es: ".$media_presion."KPa"."<br>";
$copia_presion_semanal=$Presion_semanal;
sort($copia_presion_semanal);
if ($long==0) {
	$dato_intermedio=intval($long/2);
	$dato_intermedio_1=intval($dato_intermedio-1);
	$mediana=($copia_presion_semanal[$dato_intermedio]+$copia_presion_semanal[$dato_intermedio_1])/2;
}
else {
	$numero_en_lista=intval($long/2);
	$mediana=$copia_presion_semanal[$numero_en_lista];
}
print "La mediana es: ".$mediana."KPa"."<br>";

//Punto 4

$suma_mayor=0;
$suma_menor=0;
for ($i=0;$i<$long;$i++){
	if ($Presion_semanal[$i]>$media_presion) {
		$suma_mayor+=1;
	}
	else {
		$suma_menor+=1;
	}
}
$presion_mayor_menor_media=[$suma_mayor,$suma_menor];
print "La cantidad de semanas en las que la presión promedio semanal supera la media es ".$presion_mayor_menor_media[0]."<br>";
print "La cantidad de semanas en las que la presión promedio semanal está por debajo de la media es ".$presion_mayor_menor_media[1]."<br>";

//Punto 6.1

$temperatura_prom=[];
$semana=1;
for ($i=0;$i<$long;$i++) {
	$temperatura=round(($Presion_semanal[$i]*510)/(17.16*0.082),2);
	print "La temperatura promedio para la semana ".$semana." es: ".$temperatura."K"."<br>";
	$temperatura_prom[$i+1]=$temperatura;
	$semana+=1;
}

//Punto 6.2

$long=count($temperatura_prom);
$suma=0;
for ($i=0;$i<$long+1;$i++) {
	$suma+=$temperatura_prom[$i];
}
$media_temperatura=$suma/$long;
$suma=0;
for ($i=1;$i<$long+1;$i++) {
	$suma+=($temperatura_prom[$i]-$media_temperatura)**2;
}
$varianza=$suma/$long;
$desviacion_estandar=round($varianza**0.5,2);
print "La desviación estandar de las temperaturas promedio semanales es: ".$desviacion_estandar."K"."<br>";

//Punto 6.3

$temperatura_mayor=[];
$temperatura_menor=[];
$cont_mayor=0;
$cont_menor=0;
for ($i=0;$i<$long+1;$i++) {
	if ($temperatura_prom[$i]>$media_temperatura) {
		$temperatura_mayor[$cont_mayor]=$temperatura_prom[$i];
		$cont_mayor+=1;
	} else {
		$temperatura_menor[$cont_menor]=$temperatura_prom[$i];
		$cont_menor+=1;
	}
}
$lista_de_lista_temp=[$temperatura_mayor,$temperatura_menor];

//Punto 6.4

$long_mayor=count($temperatura_mayor);
$suma_mayor=0;
for ($i=0;$i<$long_mayor;$i++) {
	$suma_mayor+=$temperatura_mayor[$i];
}
$media_mayor=$suma_mayor/$long_mayor;

$suma_mayor=0;
for ($i=0;$i<$long_mayor;$i++) {
	$suma_mayor+=($temperatura_mayor[$i]-$media_mayor)**2;
}
$varianza_mayor=$suma_mayor/($long_mayor-1);
$desviacion_estandar_mayor=round($varianza_mayor**0.5,2);
print "La desviación estandar para las temperaturas mayores a la media es: ".$desviacion_estandar_mayor."k"."<br>";

$long_menor=count($temperatura_menor);
$suma_menor=0;
for ($i=0;$i<$long_menor+1;$i++) {
	$suma_menor+=$temperatura_menor[$i];
}
$media_menor=$suma_menor/($long_menor-1);
$suma_menor=0;
for ($i=1;$i<$long_menor;$i++) {
	$suma_menor+=($temperatura_menor[$i]-$media_menor)**2;
}
$varianza_menor=$suma_menor/($long_menor-2);
$desviacion_estandar_menor=round($varianza_menor**0.5,2);
print "La desviación estandar para las temperaturas que no superan la media es: ".$desviacion_estandar_menor."k"."<br>";

//Punto 5

$media_desviacion_mayor_menor=($desviacion_estandar_mayor+$desviacion_estandar_menor)/2;
$diferencia_desviaciones=round(($desviacion_estandar)-($media_desviacion_mayor_menor),2);
print "La diferencia entre la desviación estandar encontrada en el punto 6.2 y la desviación estandar encontrada en el punto anterior es: ".$diferencia_desviaciones."K";
?>
