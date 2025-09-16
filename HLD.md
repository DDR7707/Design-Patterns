Microservies for each type
API Gateways
Cache layers for frequently accessed products
	Write through
	Read write
Load balancers
CDN for static content
Async message queues for Notifications and Orders, Inventory services
Monitoring and Analytics for performance
Database sharding and replication


Handeling concurrency:
Optimistic - Less conflicts (Validation at end)
Pesimistic - More conflicts (Locks)

Isolation Levels:
Says how concurrently running transactions effect each other.
    Read uncommited
    Read commited
    Repeatable reads
    Serializable



Error handeling
Fallback mechanism using circuit breaks
Rate limiting
Gracefull degrade (Allow only some services when others are down. Only browsring products, not adding to cart)
Retry logics


Auto scaling
Load testing
Database optimizations with indexing
content cacheing
user session management across multiple instances
Session persistence - Stickeness so that requests will be routed to same server.
compress media files for storage optimization
for video, encode for each resolution type


Problem-1: There is a sale about to be live design a system to handle users (millions), afer all the components needed he wanted to connect the flow and provide both happy and unhappy flow and in detail what all strategies to smoothly handle such traffic (only HLD)
