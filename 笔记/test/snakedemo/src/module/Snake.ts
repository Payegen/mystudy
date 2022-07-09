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

       this.head.style.left = value + 'px'
    }
    set Y(value){
        if (this.Y == value){
            return
        }
 
        if(value >= 294 || value < 0){
           throw new Error('撞墙了')
        }
 
        this.head.style.top = value + 'px'
    }

    addbodies(){
       this.element.insertAdjacentHTML('beforeend',`<div id="shenti"></div>`)
    }
    movebody(){
      

    }
}
export default Snake;