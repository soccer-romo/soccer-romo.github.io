var httpNextFiveRequest = new XMLHttpRequest();
httpNextFiveRequest.open('get', 'https://launchlibrary.net/1.4/launch?next=5')
httpNextFiveRequest.send(null);

var httpFalconRequest = new XMLHttpRequest();
httpFalconRequest.open('get', 'https://launchlibrary.net/1.4/launch?name=falcon&next=5');
httpFalconRequest.send(null);

var httpArianeRequest = new XMLHttpRequest();
httpArianeRequest.open('get', 'https://launchlibrary.net/1.4/launch?name=ariane&next=5')
httpArianeRequest.send(null);

var httpLauncheroneRequest = new XMLHttpRequest();
httpLauncheroneRequest.open('get', 'https://launchlibrary.net/1.4/launch?name=launcherone&next=5')
httpLauncheroneRequest.send(null);


fiveRocketLaunches = document.getElementById('nextFiveLaunches')
falconFiveLaunches = document.getElementById('falconFiveLaunches')
arianeFiveLaunches = document.getElementById('arianeFiveLaunches')
launcheroneFiveLaunches = document.getElementById('launcheroneFiveLaunches')
launch = document.getElementById('Launches');




fiveRocketLaunches.addEventListener('click',NextFiveLaunches)
falconFiveLaunches.addEventListener('click',FalconLaunches)
arianeFiveLaunches.addEventListener('click',ArianeLaunches)
launcheroneFiveLaunches.addEventListener('click',LauncheroneLaunches)



function NextFiveLaunches()
{
    launch.innerHTML = ""
    console.log('next 5 events')
    if(httpNextFiveRequest.readyState == 4 && httpNextFiveRequest.status == 200)
    {
        var fiveLaunches = httpNextFiveRequest.responseText;

        var fiveRocObj = JSON.parse(fiveLaunches);

        for(var i = 0; i < fiveRocObj.launches.length; i++)
        {
            var sec = document.createElement('SECTION');
            var dateLaunch = document.createElement('H1');
            var name = document.createElement('P');
            dateLaunch.innerHTML = fiveRocObj.launches[i].net;
            name.innerHTML = fiveRocObj.launches[i].name;

            sec.appendChild(dateLaunch);
            sec.appendChild(name);
            launch.appendChild(sec)
        }
    }

}

function FalconLaunches()
{
    launch.innerHTML = ""
    console.log("I've been clicked")
    if(httpFalconRequest.readyState == 4 && httpFalconRequest.status == 200)
    {
        var falcons = httpFalconRequest.responseText;

        var falconObj = JSON.parse(falcons);

        for(var i = 0; i < falconObj.launches.length; i++)
        {
            var sec = document.createElement('SECTION');
            var dateLaunch = document.createElement('H1');
            var name = document.createElement('P');
            dateLaunch.innerHTML = falconObj.launches[i].net;
            name.innerHTML = falconObj.launches[i].name;

            sec.appendChild(dateLaunch);
            sec.appendChild(name);
            launch.appendChild(sec)
        }
    }
}

function ArianeLaunches()
{
    launch.innerHTML = "";
    if(httpArianeRequest.readyState == 4 && httpArianeRequest.status == 200)
    {
        var ariane = httpArianeRequest.responseText;

        var arianeObj = JSON.parse(ariane);

        for(var i = 0; i < arianeObj.launches.length; i++)
        {
            var sec = document.createElement('SECTION');
            var dateLaunch = document.createElement('H1');
            var name = document.createElement('P');
            dateLaunch.innerHTML = arianeObj.launches[i].net;
            name.innerHTML = arianeObj.launches[i].name;

            sec.appendChild(dateLaunch);
            sec.appendChild(name);
            launch.appendChild(sec) 
        }
    }
}

function LauncheroneLaunches()
{
    launch.innerHTML = "";
    if(httpLauncheroneRequest.readyState == 4 && httpLauncheroneRequest.status == 200)
    {
        var launcherone = httpLauncheroneRequest.responseText;

        var launcheroneObj = JSON.parse(launcherone);

        for(var i = 0; i < launcheroneObj.launches.length; i++)
        {
            var sec = document.createElement('SECTION');
            var dateLaunch = document.createElement('H1');
            var name = document.createElement('P');
            dateLaunch.innerHTML = launcheroneObj.launches[i].net;
            name.innerHTML = launcheroneObj.launches[i].name;

            sec.appendChild(dateLaunch);
            sec.appendChild(name);
            launch.appendChild(sec) 
        }
    }
}
// work in progress
function updateCountdown(objectlaunch)
{
    var dateLaunch = new Date();
    var dateFrom = Date.UTC(dateToday.getFullYear(),dateToday.getMonth(),
    dateToday.getHours(),dateToday.getMinutes(),
    dateToday.getSeconds());

    var dateTo = Date.UTC(objectlaunch.launches[0].net)
    
}

