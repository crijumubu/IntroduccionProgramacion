<?php

$Utilidad = array(27834000000,23789000000,30189000000,30967000000,32501000000,32701000000,31665000000,17155000000,4614000000,834000000);

//Punto 1

function diferencia1($Utilidad)
{
// Media de la utilidad operacional de los dos primeros años de registro
	$suma1 = 0;
	$cont1 = 0;
	for ($i1=0;$i1<2;$i1++)
	{
		$suma1 = $suma1+$Utilidad[$i1];
		$cont1++;
	}
	$media1 = $suma1/$cont1;

// Media de la utilidad operacional de los dos últimos años de registro
	$suma2 = 0;
	$cont2 = 0;
	for ($i2=8;$i2<10;$i2++)
	{
		$suma2 = $suma2+$Utilidad[$i2];
		$cont2++;
	}
	$media2 = $suma2/$cont2;
	
//Diferencia de la media de utilidad operacional entre los dos ultimos años y los dos primeros años de registro
	$diferencia2 = $media1-$media2;
	return $diferencia2;
}
print "La diferencia de la media en la utilidad operacional de Kellog's en los últimos dos años comparada con la de los primeros dos años de registro es ".diferencia1($Utilidad)."COP"."<br>";
	
//Punto 2

function diferencia3($Utilidad)
{
//Año con mayor utilidad operacional
	$mayor = $Utilidad[0]; 
	for ($i3=1;$i3<10;$i3++)
	{
		if ($mayor<$Utilidad[$i3])
		{
			$mayor = $Utilidad[$i3];
		}
	}

//Año con menor utilidad operacional
	$menor = $Utilidad[0];
	for ($i4=1;$i4<10;$i4++)
	{
		if ($menor>$Utilidad[$i4])
		{
			$menor = $Utilidad[$i4];
		}
	}
	
//Diferencia entre las utilidades operacionales del año con mayor utilidad y el año con menor utilidad
	$diferencia4 = $mayor-$menor;
	return $diferencia4;
}
print "La diferencia entre las utilidades operacionales del año con mayor utilidad y el año con menor utilidad es ".diferencia3($Utilidad)." COP"."<br>";

//Punto 3

function mediana($Utilidad)
{
	sort($Utilidad);
	$mediana = ($Utilidad[4]+$Utilidad[5])/2;
	return $mediana;
}
	
print "La mediana es: ".mediana($Utilidad)."COP"."<br>";

//Punto 4

function media_mediana($Utilidad)
{
//Media
	$suma3 = 0;
	$cont5 = 0;
	for ($i5=0;$i5<10;$i5++)
	{
		$suma3 = $suma3+$Utilidad[$i5];
		$cont5++;
	}
	$media = $suma3/$cont5;
	
//Mediana
	sort($Utilidad);
	$mediana = ($Utilidad[4]+$Utilidad[5])/2;
	print "La media es: ".$media."COP"."<br>"."La mediana es: ".$mediana."COP"."<br>";
}

media_mediana($Utilidad);

//Punto 5

function porcentaje_utilidad($Utilidad)

//Utilidad operacional acumulado
{	
	$suma4 = 0;
	$año = 2008;
	for ($i6=0;$i6<10;$i6++)
	{
		$suma4 = $suma4+$Utilidad[$i6];
	}

//Utilidad operacional de cada año y porcentaje que aporta
	for ($i7=0;$i7<10;$i7++)
	{
		$porcentaje_que_aporta = round((($Utilidad[$i7]/$suma4)*100),2);
		print "El porcentaje que le aporta la utilidad operacional del año ".$año." es:".$porcentaje_que_aporta."%%"."<br>";
		$año++;
	}
}
porcentaje_utilidad($Utilidad);
	
//Punto 6

function deficit($Utilidad)
{
	$deficit = 0;
	for ($i8=8;$i8<10;$i8++)
	{
		$deficit = abs($Utilidad[$i8]-$deficit);
	}
	return $deficit;
}

print "El déficit operacional del año 2017 con respecto al año anterior es: ".deficit($Utilidad)." COP"."<br>";

//Punto7

function deficit_cada_año($Utilidad)
{
//Hallamos la media
	$suma6 = 0;
	$cont7 = 0;
	for ($i9=0;$i9<10;$i9++)
	{
		$suma6 = $suma6+$Utilidad[$i9];
		$cont7++;
	}
	$media = $suma6/$cont7;
	
//Hallamos el déficit operecaional de cada año con respecto a la media
	$año = 2008;
	for ($i10=0;$i10<10;$i10++)
	{
		$deficit1 = round(((($media - $Utilidad[$i10])/$media)*100),2);
		if ($deficit1<0)
		{
			print "El año ".$año." no tuvo un déficit operacional ya que está por éncima de la media"."<br>";
		}
		else
		{
			print "El déficit operacional del año ".$año." es: ".$deficit1."%"."<br>";
		}
		$año++;
	}
}

deficit_cada_año($Utilidad)

?>
