const Koa = require('koa')
const app = new Koa();
const Router = require('koa-router');
const routers = new Router()
const KoaBodyParser = require('koa-bodyparser');
const Parameter = require('koa-parameter');
const { Client } = require('groa');
const client = new Client('0.0.0.0', 2000);//连接服务器
app.use(Parameter(app));
app.use(KoaBodyParser())
routers.post('/test', async (ctx) => {
    const { pic } = ctx.request.body
    await client.loadProto('test.proto');//先开始加载protobuf
    // Get service defnined
    let Hello = client.getService('test.Hello');//连接hello服务

    // call
    let ret = await Hello.helloLys({
        pic : pic
    });//注意服务需要小写首字母（这是服务中的rpc）
    ctx.body = ret.result

})
app.use(routers.routes())
    .use(routers.allowedMethods())
app.listen(8080, () => {
    console.log('服务器在8080端口启动')
})
