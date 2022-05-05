
#include <boost/array.hpp>
#include <boost/bind.hpp>
#include <boost/foreach.hpp>
#include <boost/range/iterator_range.hpp>
#include <boost/python.hpp>
void add_callback(PyObject *callback)
{
}
void add_callback_cancel_packet(USBDevice *dev, USBPacket *p)
{
}
void add_callback_handle_attach(USBDevice *dev)
{
}
void add_callback_handle_reset(USBDevice *dev)
{
}
void add_callback_handle_control(USBDevice *dev, USBPacket *p, int request, int value, int index, int length, uint8_t *data)
{
}
void add_callback_handle_data(USBDevice *dev, USBPacket *p)
{
}
void add_callback_set_interface(USBDevice *dev, int interface, int alt_old, int alt_new)
{
}
void flush_ep_queue(USBDevice *dev, USBEndpoint *ep)
{
}
void add_callback_ep_stopped(USBDevice *dev, USBEndpoint *ep)
{
}
void add_callback_alloc_streams(USBDevice *dev, USBEndpoint **eps, int nr_eps, int streams)
{
}
void add_callback_free_streams(USBDevice *dev, USBEndpoint **eps, int nr_eps)
{
}

// USBPort
void add_callback_attach(USBPort *port)
{
}
void add_callback_detach(USBPort *port)
{
}
void add_callback_child_detach(USBPort *port, USBDevice *child)
{
}
void add_callback_wakeup(USBPort *port)
{
}
void add_callback_complete(USBPort *port, USBPacket *p)
{
}
