class Snake {
    // 蛇容器的元素
    element: HTMLElement;

    head:HTMLElement;

    bodies:HTMLCollection;

    constructor(){
        
        this.element = document.getElementById('snake')!;
        this.head = this.element.querySelector('#snake > div')!;
        this.bodies = this.element.getElementsByTagName('div');

        if(this.element!==null){
            console.log('snake初始化ok');
        }else{
            console.log('失败');
            
        }
    }

    get X(){
        return this.head.offsetLeft;
    }
    get Y(){
        return this.head.offsetTop;
    }

    set X(value){
       if (this.X == value){
           return
       }

       
       if(value >= 294 || value < 0){
          throw new Error('撞墙了')
       }

       if(this.bodies.length>1 && (this.bodies[1] as HTMLElement).offsetLeft === value){
        //将要赋值的值是第二个元素的位置则为反向移动了
        if(value < this.X){
            value = this.X + 10 
        }else{
            value = this.X - 10
        }
       }
       this.movebody();
       this.head.style.left = value + 'px';
       this.checkHeadBody();
       
    }
    set Y(value){
        if (this.Y == value){
            return
        }
 
        if(value >= 294 || value < 0){
           throw new Error('撞墙了')
        }

        if(this.bodies.length>1 && (this.bodies[1] as HTMLElement).offsetTop === value){
            if(value < this.Y){
                value = this.Y + 10 
            }else{
                value = this.Y - 10
            }
         
        }

        //此处移动身体在移动头部之前，不然第二个元素就和头部重合了
        this.movebody();
        this.head.style.top = value + 'px';
        this.checkHeadBody();
    }

    addbodies(){
       this.element.insertAdjacentHTML('beforeend',`<div id="shenti"></div>`)
    }
    movebody(){
       for (let index = this.bodies.length-1 ; index > 0; index--) {
        let x = (this.bodies[index-1] as HTMLElement).offsetLeft;
        let y = (this.bodies[index-1] as HTMLElement).offsetTop;

        (this.bodies[index] as HTMLElement).style.left = x + 'px';
        (this.bodies[index] as HTMLElement).style.top = y + 'px';
       }
       
    }
    checkHeadBody(){
        if(this.bodies.length>4){
            for(let i=this.bodies.length-1 ; i>0; i--){
                let bod = (this.bodies[i] as HTMLElement)
                if(bod.offsetLeft === this.X && bod.offsetTop === this.Y){
                    throw new Error("自己吃自己了！");
                }
            }
        }
    }
}
export default Snake;