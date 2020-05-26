<?php

if (isset($_POST['resultado'])) 
{
	$num = $_POST['n'];
	$c = $num-1;
	for ($i=1;$i<$num;$i++)
	{
		if ($num%$i==0)
		{
			$total = $total+$i; 
		}
	}
	if ($total==$num)
	{
		print "El número es perfecto";
	}
	else 
	{
		print "El número no es perfecto";
	}
}
?>


<html>

<body>
<form name="número perfecto" method="POST" action="laboratorio10L.php">
	Ingrese un número para determinar si este es o no un número perfecto: <input type="TEXT" name="n">
	<br><input type="submit" name="resultado" value="Ver resultado">
</form>
</body>
</html>