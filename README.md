# Voyages Évasion - Site d'Agence de Voyage Hors Ligne

## 🌍 Présentation

Site web interactif d'agence de voyage développé en HTML, CSS et JavaScript pur, conçu pour fonctionner complètement hors ligne. Le site propose une expérience utilisateur moderne et fluide avec de nombreuses fonctionnalités interactives.

## ✨ Fonctionnalités

### 🏠 Page d'Accueil
- **Hero Section** avec animation de particules flottantes
- **Barre de recherche interactive** avec validation en temps réel
- **Navigation fluide** avec scroll automatique
- **Design responsive** adapté à tous les appareils

### 🗺️ Destinations
- **12 destinations** avec images artistiques
- **Système de filtres** par continent (Europe, Asie, Amérique, Afrique, Océanie)
- **Recherche en temps réel** par nom ou caractéristiques
- **Cartes interactives** avec effets de hover et animations
- **Modales détaillées** pour chaque destination

### 🛠️ Services
- **6 services principaux** : Vols, Hébergements, Location voiture, Circuits, Assurance, Support
- **Animations d'apparition** au scroll
- **Icônes animées** avec effets de hover

### 📝 Réservation
- **Formulaire complet** avec validation avancée
- **Sauvegarde automatique** des données saisies
- **Messages de confirmation** avec animations
- **Contraintes de dates** intelligentes

### 📞 Contact
- **Formulaire de contact** fonctionnel
- **Informations pratiques** complètes
- **Validation en temps réel** des champs

## 🎨 Fonctionnalités Techniques

### Animations & Effets
- **Animations CSS3** fluides et modernes
- **Intersection Observer** pour les animations au scroll
- **Effets parallax** subtils
- **Particules flottantes** interactives
- **Transitions morphing** sur les boutons
- **Effets de tilt** sur les cartes

### Interactivité JavaScript
- **Navigation responsive** avec menu hamburger
- **Recherche instantanée** avec debouncing
- **Filtrage dynamique** des destinations
- **Validation de formulaires** en temps réel
- **Système de notifications** elegant
- **Modales dynamiques** pour les détails

### Design Responsive
- **Mobile-first** approach
- **Breakpoints optimisés** pour tous les appareils
- **Menu adaptatif** pour mobile
- **Images optimisées** pour le web
- **Typography** fluide et lisible

### Performances
- **Code optimisé** sans frameworks lourds
- **Images compressées** pour un chargement rapide
- **CSS organisé** avec variables personnalisées
- **JavaScript modulaire** et efficace
- **Animations performantes** avec requestAnimationFrame

## 🚀 Utilisation

### Installation
1. **Télécharger** tous les fichiers du projet
2. **Conserver** la structure des dossiers intacte
3. **Ouvrir** `index.html` dans votre navigateur

### Structure des Fichiers
```
agence-voyage-offline/
├── index.html              # Page principale
├── css/
│   ├── style.css           # Styles principaux
│   └── animations.css      # Animations CSS
├── js/
│   ├── data.js            # Données des destinations
│   ├── main.js            # Logique principale
│   └── animations.js      # Animations JavaScript
└── images/
    ├── hero-background.png # Arrière-plan hero
    ├── paris.png          # Image de Paris
    ├── tokyo.png          # Image de Tokyo
    └── bali.png           # Image de Bali
```

### Navigation
- **Scroll fluide** entre les sections
- **Menu responsive** qui s'adapte à l'appareil
- **Liens actifs** mis à jour automatiquement

### Recherche
- **Tapez une destination** dans la barre de recherche
- **Les résultats s'affichent** instantanément
- **Filtrez par continent** avec les boutons dédiés

### Réservation
1. **Remplir le formulaire** de réservation
2. **Les données sont sauvegardées** automatiquement
3. **Validation en temps réel** des champs
4. **Confirmation** d'envoi avec animation

## 🎯 Fonctionnalités Avancées

### Mode Sombre (Bonus)
- **Basculement automatique** selon les préférences système
- **Palette de couleurs** adaptée
- **Sauvegarde** des préférences utilisateur

### Sauvegarde Automatique
- **Formulaires sauvegardés** en localStorage
- **Récupération automatique** des données
- **Prévention de la perte** de données

### Système de Favoris
- **Ajouter des destinations** aux favoris
- **Stockage local** des préférences
- **Interface intuitive** de gestion

### Animations Intelligentes
- **Respect du prefer-reduced-motion** pour l'accessibilité
- **Animations conditionnelles** selon les performances
- **Dégradation gracieuse** sur les appareils moins puissants

## 🌟 Points Forts

### Design
- **Interface moderne** et professionnelle
- **Couleurs harmonieuses** inspirées du voyage
- **Typography** soignée avec Google Fonts
- **Iconographie** cohérente avec Font Awesome

### UX/UI
- **Navigation intuitive** et fluide
- **Feedback visuel** pour toutes les interactions
- **Messages d'erreur** clairs et utiles
- **Loading states** pour une meilleure perception

### Performance
- **Chargement rapide** sans dépendances lourdes
- **Code optimisé** pour tous les navigateurs
- **Images optimisées** pour le web
- **Animations 60fps** fluides

### Accessibilité
- **Contrastes respectés** pour la lisibilité
- **Navigation au clavier** supportée
- **Screen readers** compatibles
- **Animations réduites** si nécessaire

## 🔧 Personnalisation

### Couleurs
Modifiez les variables CSS dans `style.css` :
```css
:root {
    --primary-color: #2c5aa0;
    --secondary-color: #f39c12;
    --accent-color: #e74c3c;
    /* ... */
}
```

### Destinations
Ajoutez de nouvelles destinations dans `data.js` :
```javascript
{
    id: 13,
    nom: "Nouvelle Destination",
    pays: "Pays",
    continent: "europe",
    prix: 500,
    duree: "5 jours",
    image: "images/nouvelle-destination.png",
    description: "Description attractive...",
    caracteristiques: ["Tag1", "Tag2", "Tag3"],
    note: 4.5,
    populaire: true
}
```

### Animations
Personnalisez les animations dans `animations.css` ou ajoutez de nouveaux effets dans `animations.js`.

## 📱 Compatibilité

### Navigateurs Supportés
- ✅ Chrome 60+
- ✅ Firefox 55+
- ✅ Safari 12+
- ✅ Edge 79+

### Appareils
- ✅ Desktop (1920px+)
- ✅ Laptop (1024px+)
- ✅ Tablet (768px+)
- ✅ Mobile (320px+)

## 🎨 Technologies Utilisées

- **HTML5** - Structure sémantique
- **CSS3** - Styles et animations
- **JavaScript ES6+** - Interactivité
- **Font Awesome** - Iconographie
- **Google Fonts** - Typography

## 📄 Licence

Ce projet est développé à des fins éducatives et de démonstration. Libre d'utilisation et de modification.

---

*Créé avec ❤️ pour démontrer les possibilités du développement web moderne sans frameworks.*