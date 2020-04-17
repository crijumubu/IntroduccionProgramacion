<?php
$Supercomputadoras = array(
    array('Summit' , '2414592' , '148600' , '200794'),
    array('Sierra' , '1572480' , '94640' , '125712'),
    array('Sunway TaihuLight' , '10649600' , '93014' , '125435'),
    array('Tianhe-2A' , '4981760' , '61444' , '100678'),
    array('Frontera' , '448448' , '23516' , '38745'),
    array('Piz Daint' , '387872' , '21230' , '27154'),
    array('Trinity' , '979072' , '20158' , '41461'),
    array('AI Bridging Cloud Infrastructure (ABCI)' , '391680' , '19880' , '32576'),
    array('SuperMUC-NG' , '305856' , '19476' , '26873'),
    array('Lasen' , '288288' , '18200' , '23047')
);

//Supercomputadora con mayor núcleos

function Supercomputadora_con_más_nucleos($Supercomputadoras)
{
	$niveles = count($Supercomputadora);
	$máx = $Supercomputadoras[0][1];
	$nombre_máx_supercomputadora = $Supercomputadoras[0][0];
	for ($i=1;$i<$niveles;$i++)
	{
		if (intval($máx)<intval($Supercomputadoras[$i][1]))
		{
			$máx = $Supercomputadoras[$i][1];
			$nombre_máx_supercomputadora = $Supercomputadoras[$i][0];
		}
	}
	print "La computadora que más tiene núcleos es ". $nombre_máx_supercomputadora." y tiene ". $máx." núcleos"."<br>";
}

Supercomputadora_con_más_nucleos($Supercomputadoras);

//Supercomputadoras que superan con su menor registro de TFlops/s el valor ingresado por el usuario

function Supercomputadoras_Rmax($Supercomputadoras)
{
	if (isset($_POST['resultado'])) 
	{
		$a = intval($_POST['n']);
		$niveles = count($Supercomputadoras);
		for ($i=0;$i<$niveles;$i++)
		{
			if (intval($Supercomputadoras[$i][2])>$a)
			{
				print "Las computadoras con mas de ".$a." TFlops/s en su menor registro son:"."<br>";
				break;
			}
			else
			{
				print "No hay ninguna supercomputadora con mas de ".$a." TFlops/s en su menor registro";
				break;
			}
		}
		for ($i=0;$i<$niveles;$i++)
		{
			if (intval($Supercomputadoras[$i][2])>$a)
			{
				print $Supercomputadoras[$i][0]."<br>";
			}
		}
	
	}
}

Supercomputadoras_Rmax($Supercomputadoras);

//Promedio de cada una de las supercomputadoras de su mínimo TFlops/s registrado y su máximo TFlops/s registrado

function Supercomputadoras_promedio($Supercomputadoras)
{
	$niveles = count($Supercomputadoras);
	$columnas = (count($Supercomputadoras,1)-$niveles)/$niveles;
	$suma = 0;
	$cont = 0;
	for ($nivel=0;$nivel<$niveles;$nivel++)
	{
		for ($columna=2;$columna<$columnas;$columna++)
		{
			if ($columnas-1==$columna)
			{
				$suma = $suma+intval($Supercomputadoras[$nivel][$columna]);
				$cont = $cont+1;
				$promedio = $suma/$cont;
			}
			else
			{
				$suma = $suma+intval($Supercomputadoras[$nivel][$columna]);
				$cont = $cont+1;
			}
		}
		print "El promedio de TFlops/s de la supercomputadora ".$Supercomputadoras[$nivel][0]."es: ".round($promedio,2)."<br>";
	}
}

Supercomputadoras_promedio($Supercomputadoras)
?>

<html>

<body>
<form name="Supercomputadoras_TFlops/s" method="POST" action="Preinforme11L_CristianMuñoz.php">
	Ingrese un valor para determinar cuales supercomputadoras superan este valor con su menor registro de TFlops/s, recuerde que el valor que ingrese solo influirá en la respuesta a la segunda pregunta	<input type="TEXT" name="n">
	<br><input type="submit" name="resultado" value="Ver resultado">
</form>
</body>
</html>