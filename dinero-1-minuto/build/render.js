const { chromium } = require('playwright');
const fs=require('fs'); const {spawn}=require('child_process');
(async()=>{
  const tl=fs.readFileSync(__dirname+'/timeline.json','utf8');
  const html=fs.readFileSync(__dirname+'/escena.html','utf8').replace('__TIMELINE__',tl);
  fs.writeFileSync(__dirname+'/_page.html',html);
  const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1080,height:1920}});
  await p.goto('file://'+__dirname+'/_page.html'); await p.waitForTimeout(500);
  const mode=process.argv[2];
  if(mode==='stills'){
    for(const t of process.argv.slice(3)){await p.evaluate(t=>render(t),+t);await p.screenshot({path:`${__dirname}/../stills/f_${t}.jpg`,type:'jpeg',quality:80});}
  } else {
    const fps=30,total=JSON.parse(tl).total,N=Math.ceil(total*fps);
    const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate',''+fps,'-c:v','mjpeg','-i','-','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p',__dirname+'/video_mudo.mp4'],{stdio:['pipe','inherit','inherit']});
    for(let i=0;i<N;i++){await p.evaluate(t=>render(t),i/fps);const buf=await p.screenshot({type:'jpeg',quality:92});
      if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r)); if(i%150==0)console.log(i,'/',N);}
    ff.stdin.end(); await new Promise(r=>ff.on('close',r));
  }
  await b.close();
})();
