<?php
if (isset($_POST['matiere']) && isset($_POST['professeur']) && isset($_POST['heureTotale']) && isset($_POST['jour'])) {
  // Récupérer les données du formulaire
  $matiere = $_POST['matiere'];
  $professeur = $_POST['professeur'];
  $heureTotale = $_POST['heureTotale'];
  $jour = $_POST['jour'];

  // Vérifier si le fichier CSV existe
  $fileExists = file_exists('emplois.csv');

  // Ouvrir le fichier CSV en mode écriture
  $file = fopen('emplois.csv', 'a');

  // Écrire les données dans le fichier CSV
  if (!$fileExists) {
    // Écrire l'en-tête des colonnes si le fichier n'existe pas
    fputcsv($file, array('Matière', 'Professeur', 'Heure totale', 'Heure restante', 'Jour'));
  }

  // Calculer l'heure restante
  $heureRestante = $heureTotale;

  // Vérifier si la matière existe déjà dans le fichier CSV
  $matiereExists = false;
  if (($handle = fopen('emplois.csv', 'r')) !== false) {
    while (($data = fgetcsv($handle)) !== false) {
      if ($data[0] == $matiere) {
        $heureRestante = intval($data[3]) - $heureTotale;
        $matiereExists = true;
        break;
      }
    }
    fclose($handle);
  }

  // Écrire la ligne de données dans le fichier CSV
  fputcsv($file, array($matiere, $professeur, $heureTotale, $heureRestante, $jour));

  // Fermer le fichier CSV
  fclose($file);

  // Afficher les emplois du temps mis à jour dans le tableau
  $emplois = array();

  if (($handle = fopen('emplois.csv', 'r')) !== false) {
    while (($data = fgetcsv($handle)) !== false) {
      $emplois[] = $data;
    }
    fclose($handle);
  }

  foreach ($emplois as $emploi) {
    echo '<tr>';
    echo '<td>' . $emploi[0] . '</td>';
    echo '<td>' . $emploi[1] . '</td>';
    echo '<td>' . $emploi[2] . '</td>';
    echo '<td>' . $emploi[3] . '</td>';
    echo '<td>' . $emploi[4] . '</td>';
    echo '<td><button class="btn btn-sm btn-primary edit-btn">Modifier</button></td>';
    echo '</tr>';
  }
}
?>
