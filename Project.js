//Maria del Carmen Bravo Gonzalez-Blas // Master of Bioinformatics (KU Leuven)
//r0442162


//Load the google packages.
google.charts.load('current', {'packages':['geochart']});

//For the interactive maps to drawn (continuous loading).
google.charts.setOnLoadCallback(drawRegionsMap);
google.charts.setOnLoadCallback(setup);


//Load the data.      
var matrix;
function preload() {
  matrix = loadTable("CountryMatrix.csv", "csv", "header");
}


//Define value arrays.
var addiction = [];
var autoinmune = [];
var cancer = [];
var cardiovascular = [];
var female = [];
var gastrointestinal = [];
var genetic = [];
var neurodegenerative = [];
var neurophysiological = [];
var neurophysiologicaltrait = [];
var other = [];
var diseasearray = ["Disease"];
var typearray = ["Type"];

//Setup. 
function setup(){
  
  //To draw initial map in white when the page is opened.
  var data = google.visualization.arrayToDataTable([['Country', 'Risk'], ['-','-']]);

  var options = {
    colorAxis: {colors: ['green', 'yellow', 'red']},
    backgroundColor: '#81d4fa',
    datalessRegionColor: 'white',
    defaultColor: '#f5f5f5',
  };

  var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

  chart.draw(data, options);
  
  //To complete value arrays.
  for (var i = 1; i < matrix.getRowCount(); i++){
    var type = matrix.get(i,0);
    var disease = matrix.get(i,1);
    typearray.push(type);
    diseasearray.push(disease);
    if (type == "Addiction"){
      addiction.push(disease);
    }
    if (type == "Autoinmune"){
      autoinmune.push(disease);
    }
    if (type == "Cancer"){
      cancer.push(disease);
    }
    if (type == "Cardiovascular"){
      cardiovascular.push(disease)
    }
    if (type == "Female"){
      female.push(disease);
    }
    if (type == "Gastrointestinal"){
      gastrointestinal.push(disease);
    }
    if (type == "Genetic "){
      genetic.push(disease);
    }
    if (type == "Neurodegenerative"){
      neurodegenerative.push(disease);
    }
    if (type == "Neurophysiological"){
      neurophysiological.push(disease);
    }
    if (type == "Neurophysiological Trait"){
      neurophysiologicaltrait.push(disease);
    }
    if (type == "Other"){
      other.push(disease);
    }
  }

  //To enable drawing/writing.
  createCanvas(1000, 1000); 
  

  //Text. text2 and text4 will be completed with the chosen type and disease, respectively.
  text1 = createDiv('Selected type of disease/trait:');
  text1.position(950,150);
  
  text2 = createDiv('');
  text2.position(950,200);
  
  text3 = createDiv('Selected disease/trait:');
  text3.position(950,250);
  
  text4 = createDiv('');
  text4.position(950,300);
  
  //Description.
  text5 = createDiv('Given a type and a disease/trait, the map represents how likely is in average in each country to develop a disease/trait given the genotype of the patients from that country available. The higher score, the more chances to develop the disease/trait. The scale is shown on the bottom left of the map. Exact values for each country can be seen by positioning the mouse on them.');
  //text5.position(950,400);
  text5.position(10,580);
}

//Contains the groups of disease corresponding to each type. In this way, when selecting the correponding type,
//the corresponding diseases will be displayed.
var Select_List_Data = {
  'Disease': { // Name of associated select box
      Type: {text: ["----Select Disease----"]},
      Addiction: {text: addiction, value: addiction},
      Autoinmune: {text: autoinmune, value: autoinmune},
      Cancer: {text: cancer, value: cancer},
      Cardiovascular: {text: cardiovascular, value: cardiovascular}, 
      Female: {text: female, value: female},
      Gastrointestinal: {text: gastrointestinal, value: gastrointestinal},
      Genetic: {text: genetic, value: genetic},
      Neurodegenerative: {text: neurodegenerative, value: neurodegenerative},
      Neurophysiological: {text: neurophysiological, value: neurophysiological},
      Neurophysiological_Trait: {text: neurophysiologicaltrait, value: neurophysiologicaltrait},
      Other: {text: other, value: other},
  }    
};



//Removes all option elements in select box.
function removeAllOptions(sel) {
    var len = sel.options.length;
    for (var i=len; i; i--) {
        par = sel.options[i-1].parentNode;
        par.removeChild( sel.options[i-1] );
    }
};

//Given a selection attaches the corresponding diseases for the selected type.
function appendDataToSelect(sel, obj) {
    var f = document.createDocumentFragment();
    var labels = [], group, opts;

    function addOptions(obj) {
        var f = document.createDocumentFragment();
        var o;
        
        for (var i=0, len=obj.text.length; i<len; i++) {
            o = document.createElement('option');
            o.appendChild( document.createTextNode( obj.text[i] ) );
            
            if ( obj.value ) {
                o.value = obj.value[i];
            }
            
            f.appendChild(o);
        }
        return f;
    }
    
    if ( obj.text ) {
        opts = addOptions(obj);
        f.appendChild(opts);
    } else {
        for ( var prop in obj ) {
            if ( obj.hasOwnProperty(prop) ) {
                labels.push(prop);
            }
        }
    }
    sel.appendChild(f);
};

// Populate associated select box as page loads.
window.onload = function() { // Immediate function to avoid globals.
    
    var form = document.forms['Form'];
    
    // Reference to controlling select box.
    var sel = form.elements['Type'];
    sel.selectedIndex = 0;
    
    // Name of associated select box.
    var relName = 'Disease';
    
    // Reference to associated select box.
    var rel = form.elements[ relName ];
    
    // Get data for associated select box passing its name and value of selected in controlling select box.
    var data = Select_List_Data[ relName ][ sel.value ];
    
    // Add options to associated select box.
    appendDataToSelect(rel, data);
    
};


//Draw map.    
function drawRegionsMap() {
  // Anonymous function assigned to onchange event of controlling select box.
  document.forms['Form'].elements['Type'].onchange = function(e) {
    // Name of associated select box.
    var relName = 'Disease';
    
    // Reference to associated select box. 
    var relList = this.form.elements[ relName ];
    
    // Get data from object literal based on selection in controlling select box.
    var obj = Select_List_Data[ relName ][ this.value ];
    
    // Remove current option elements.
    removeAllOptions(relList, true);
    
    // Call function to add option elements pass reference to associated select box and data for new options.
    appendDataToSelect(relList, obj);
  };
  
  // Anonymous function assigned to onchange event of associated select box.
  document.forms['Form'].elements['Disease'].onchange = function(e) {
    //Get value of the selected type and disease.
    var t = document.getElementById("Type");
    var valuet = t.options[t.selectedIndex].value;
    var d = document.getElementById("Disease");
    var valued = d.options[d.selectedIndex].value;
    
    // As "Neurophysiological Trait" value could not include " ", it was set to "Neurophysiological_Trait"
    // It is necessary to change the value to "Neurophysiological Trait" in order to perform the folowwing index
    // operations.
    if (valuet == "Neurophysiological_Trait"){
      valuet = "Neurophysiological Trait";
    }
 
    //Refresh the type and disease dispayed name.
    text2.remove()  
    text2 = createDiv(valuet);
    text2.position(950,200);
    text4.remove()  
    text4 = createDiv(valued);
    text4.position(950,300);
  
    //Containers for country/points data for the given disease. Get index of the corresponding row in the matrix.
    //Since "All diseases/traits" is included for all groups, a start position is defined in order to select the
    //corresponding row.
    var array = [['Country', 'Risk']];
    var country;
    var punctuation;
    var start = typearray.indexOf(valuet);
    var index = diseasearray.indexOf(valued, start);
    if (valuet == "Genetic"){
      index = diseasearray.indexOf("Haemochromatosis");
    }
    var type = matrix.get(index, 0);

    //Fill containers.
    for (var i = 2; i < matrix.getColumnCount(); i++){
      punctuation = float(matrix.get(index,i));
      country = matrix.get(0,i);
      array.push([country, punctuation]);
    };

    //Draw map according to the data.
    var data = google.visualization.arrayToDataTable(array);

    var options = {
      colorAxis: {colors: ['green', 'yellow', 'red']},
      backgroundColor: '#81d4fa',
      datalessRegionColor: 'white',
      defaultColor: '#f5f5f5',
    };

    var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

    chart.draw(data, options);
  };

}