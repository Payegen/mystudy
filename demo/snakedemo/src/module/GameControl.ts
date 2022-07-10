import Snake from "./Snake";
import Food from "./Food";
class GameControl{
    snake:Snake;
    food:Food;
    isLive:boolean =true;
    // 记录移动方向
    target:string = 'ArrowDown';

    constructor(){
        this.snake = new Snake();
        this.food = new Food();
        this.init();
    }

    init(){       
        document.addEventListener('keydown', this.thisHandler.bind(this));
        this.move()
    }
    thisHandler(e:KeyboardEvent){
        this.target = e.key;
    }
    move(){
        let X = this.snake.X;
        let Y = this.snake.Y;
 //       console.log(this.target);
      
        switch (this.target) {
            case "ArrowUp":
                // console.log(Y);
                Y -= 10;
                break; 
            case "ArrowDown":
                // console.log(Y);
                Y += 10;
                break;
            case "ArrowLeft":
                // console.log(X);
                X -= 10;
                break;
            case "ArrowRight":
                // console.log(X);
                X += 10;
                break;
            default:
                break;
        }
        
        this.eatfood(X,Y);

        try {
            this.snake.X = X;
            this.snake.Y = Y;
        } catch (e:any) {
            // 进入到catch，说明出现了异常，游戏结束，弹出一个提示信息
            alert(e.message + ' GAME OVER!');
            // 将isLive设置为false
            this.isLive = false;
        }
        clearTimeout();
        this.isLive && setTimeout(this.move.bind(this),300)
    }

    eatfood(x:number,y:number): boolean{
       
       if(x === this.food.X && y === this.food.Y){
        console.log('吃到了');
        this.snake.addbodies();
        return true
       }
       return false
    }
}
export default GameControl;