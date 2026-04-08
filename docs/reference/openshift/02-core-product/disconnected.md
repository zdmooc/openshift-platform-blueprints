# Installations Déconnectées & en Air Gap

## Objectif

Cette section explique comment installer et gérer un cluster OpenShift dans un environnement déconnecté (ou en "air gap"), c'est-à-dire un environnement sans accès direct à Internet. C'est un cas d'utilisation courant dans les secteurs de la finance, de la défense et du gouvernement.

## Concepts

L'exécution d'un cluster OpenShift en mode déconnecté nécessite de mettre en miroir tout le contenu nécessaire (images de conteneurs, packages RPM, etc.) depuis Internet vers un registre privé accessible par le cluster.

### Mise en miroir du contenu

Le processus de mise en miroir consiste à copier les images de conteneurs requises pour l'installation et la mise à jour d'OpenShift depuis les registres de Red Hat (`registry.redhat.io`, `quay.io`) vers un registre local.

- **`oc-mirror`** : Un nouvel outil en ligne de commande qui simplifie le processus de mise en miroir. Il permet de créer et de publier un "image set" qui contient tout le nécessaire pour une version d'OpenShift.
- **Registre miroir** : Un registre de conteneurs que vous hébergez dans votre environnement déconnecté. Tous les nœuds du cluster doivent pouvoir y accéder.

### Processus d'installation déconnectée

1. **Sur une machine connectée** : Utilisez `oc-mirror` pour créer un miroir du contenu d'une version d'OpenShift.
2. **Transférer le contenu** : Copiez le contenu mis en miroir de la machine connectée vers l'environnement déconnecté (par ex., via un disque dur externe).
3. **Publier sur le registre local** : Poussez le contenu mis en miroir vers votre registre local.
4. **Configurer l'installateur** : Modifiez le fichier `install-config.yaml` pour qu'il pointe vers votre registre miroir local.
5. **Lancer l'installation** : Exécutez `openshift-install create cluster`.

### Mise à jour d'un cluster déconnecté

La mise à jour d'un cluster déconnecté suit un processus similaire : vous mettez en miroir le contenu de la nouvelle version, vous le publiez sur votre registre local, puis vous lancez la mise à jour via la console web ou la CLI.

## Où chercher dans la documentation officielle

- **Mise en miroir des images pour une installation déconnectée** : [https://docs.openshift.com/container-platform/latest/installing/disconnected_install/mirroring-installation-images.html](https://docs.openshift.com/container-platform/latest/installing/disconnected_install/mirroring-installation-images.html)
- **Mise à jour d'un cluster déconnecté** : [https://docs.openshift.com/container-platform/latest/updating/updating-disconnected-cluster.html](https://docs.openshift.com/container-platform/latest/updating/updating-disconnected-cluster.html)

## Commandes clés

```bash
# Créer un fichier de configuration pour oc-mirror
oc-mirror init --config imageset-config.yaml --target-oci oci://my-mirror

# Mettre en miroir les images
oc-mirror --config imageset-config.yaml oci://my-mirror

# Publier les images vers un registre local
oc-mirror --from oci://my-mirror/ --to-registry <local-registry-address>

# (Ancienne méthode) Configurer le cluster pour utiliser le miroir
oc adm release mirror -a <pull-secret-file> --to-dir=<mirror-dir> <release-version>
```

## À retenir / Pièges fréquents

- **La planification est essentielle** : Les installations déconnectées nécessitent une planification minutieuse de l'infrastructure réseau et du registre miroir.
- **L'espace de stockage** : Un miroir complet d'une version d'OpenShift, y compris les Operators, peut prendre plusieurs centaines de Go. Assurez-vous d'avoir suffisamment d'espace de stockage.
- **Le pull secret** : Vous avez besoin d'un pull secret valide de Red Hat pour télécharger les images. Ce secret doit également être configuré dans votre cluster pour qu'il puisse tirer les images depuis votre registre miroir.
- **`oc-mirror` est le nouvel outil** : Les anciennes méthodes de mise en miroir (`oc adm release mirror`) sont toujours supportées, mais `oc-mirror` est l'outil recommandé pour les nouvelles installations.
